# -*- encoding: utf-8 -*-
import datetime

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase
from model_mommy import mommy

from bpp.models import (
    Patent_Autor,
    Jednostka,
    Typ_Odpowiedzialnosci,
    Patent,
    Praca_Doktorska,
    Praca_Habilitacyjna,
    Tytul,
    Zrodlo,
    Charakter_Formalny,
    Jezyk,
    Typ_KBN,
    Status_Korekty,
    Zrodlo_Informacji,
    Wydawnictwo_Ciagle_Autor,
    Uczelnia,
    Wydzial,
)
from bpp.models.cache import Rekord, with_cache, Autorzy, AutorzyView
from bpp.tests.tests_legacy.test_reports.util import ciagle, zwarte, autor
from bpp.tests.util import any_ciagle, any_autor

CHANGED = "foo-123-changed"


def ramka(msg):
    print("+" + ("-" * 78) + "+")
    print("+ " + msg)
    print("+" + ("-" * 78) + "+")


def clean_dict(ret):
    del ret["ostatnio_zmieniony"]
    del ret["tytul_oryginalny_sort"]
    return ret


class LoadFixturesMixin:
    def loadFixtures(self):
        for db_name in self._databases_names(include_mirrors=False):
            if hasattr(self, "fixtures"):
                call_command(
                    "loaddata",
                    *self.fixtures,
                    **{"verbosity": 0, "database": db_name, "skip_validation": True}
                )


class TestCacheMixin:
    # fixtures = [
    #     'typ_odpowiedzialnosci.json', 'tytul.json', 'zrodlo_informacji.json',
    #     'charakter_formalny.json', 'status_korekty.json', 'typ_kbn.json',
    #     'jezyk.json']

    def setUp(self):
        self.maxDiff = None

        aut = Typ_Odpowiedzialnosci.objects.get(skrot="aut.")
        self.typ_odpowiedzialnosci = aut

        self.uczelnia = mommy.make(Uczelnia)
        self.wydzial = mommy.make(Wydzial, uczelnia=self.uczelnia)
        self.j = mommy.make(
            Jednostka, nazwa="Foo Bar", uczelnia=self.uczelnia, wydzial=self.wydzial
        )

        self.a = autor(self.j)
        self.a.nazwisko = "Kowalski"
        self.a.imiona = "Jan"
        self.a.tytul = Tytul.objects.get(skrot="dr")
        self.a.save()

        wspolne_dane = dict(
            adnotacje="adnotacje",
            informacja_z=Zrodlo_Informacji.objects.all()[0],
            status_korekty=Status_Korekty.objects.all()[0],
            rok="2000",
            www="http://127.0.0.1/",
            recenzowana=True,
            impact_factor=5,
            punkty_kbn=5,
            index_copernicus=5,
            punktacja_wewnetrzna=5,
            weryfikacja_punktacji=True,
            typ_kbn=Typ_KBN.objects.all()[0],
            jezyk=Jezyk.objects.all()[0],
            informacje="informacje",
            szczegoly="szczegoly",
            uwagi="uwagi",
            slowa_kluczowe="slowa kluczowe",
        )

        zwarte_dane = dict(
            miejsce_i_rok="Lublin 2012",
            wydawnictwo="Pholium",
            redakcja="Redkacja",
            isbn="isbn",
            e_isbn="e_isbn",
            tytul="tytul",
        )

        self.z = zwarte(
            self.a,
            self.j,
            aut,
            tytul_oryginalny="zwarte",
            liczba_znakow_wydawniczych=40000,
            charakter_formalny=Charakter_Formalny.objects.all()[0],
            **dict(list(zwarte_dane.items()) + list(wspolne_dane.items()))
        )

        self.zr = mommy.make(Zrodlo, nazwa="Zrodlo")

        self.c = ciagle(
            self.a,
            self.j,
            tytul_oryginalny="ciągłe",
            zrodlo=self.zr,
            tytul="tytul",
            issn="issn",
            e_issn="e_issn",
            charakter_formalny=Charakter_Formalny.objects.all()[0],
            **wspolne_dane
        )
        self.assertEqual(Wydawnictwo_Ciagle_Autor.objects.all().count(), 1)

        wca = Wydawnictwo_Ciagle_Autor.objects.all()[0]
        wca.typ_odpowiedzialnosci = self.typ_odpowiedzialnosci
        wca.save()

        settings.BPP_CACHE_ENABLED = True

        # Doktorat i habilitacja

        doktorat_kw = dict(list(zwarte_dane.items()) + list(wspolne_dane.items()))

        self.d = mommy.make(
            Praca_Doktorska,
            tytul_oryginalny="doktorat",
            autor=self.a,
            jednostka=self.j,
            **doktorat_kw
        )

        self.h = mommy.make(
            Praca_Habilitacyjna,
            tytul_oryginalny="habilitacja",
            autor=self.a,
            jednostka=self.j,
            **doktorat_kw
        )

        # Patent

        chf_pat = Charakter_Formalny.objects.get(skrot="PAT")

        for elem in ["typ_kbn", "jezyk"]:
            del wspolne_dane[elem]

        self.p = mommy.make(
            Patent,
            tytul_oryginalny="patent",
            numer_zgloszenia="100",
            data_decyzji=datetime.date(2012, 1, 1),
            **wspolne_dane
        )

        Patent_Autor.objects.create(
            autor=self.a,
            jednostka=self.j,
            rekord=self.p,
            typ_odpowiedzialnosci=aut,
            zapisany_jako="Kowalski",
        )

        self.wszystkie_modele = [self.d, self.h, self.p, self.c, self.z]


class TestCacheRebuildBug(TestCase):
    @with_cache
    def test_liczba_znakow_bug(self):
        Rekord.objects.full_refresh()
        self.assertEqual(Rekord.objects.all().count(), 0)

        c = any_ciagle(tytul="foo", liczba_znakow_wydawniczych=31337)
        Rekord.objects.full_refresh()

        self.assertEqual(Rekord.objects.all().count(), 1)
        self.assertEqual(Rekord.objects.all()[0].tytul, "foo")
        self.assertEqual(Rekord.objects.all()[0].liczba_znakow_wydawniczych, 31337)


class TestCacheSimple(TestCacheMixin, TestCase):
    def setUp(self):
        Typ_Odpowiedzialnosci.objects.get_or_create(skrot="aut.", nazwa="autor")
        Charakter_Formalny.objects.get_or_create(skrot="PAT")
        for skrot, nazwa in [("ang.", "angielski"), ("fr.", "francuski")]:
            Jezyk.objects.get_or_create(skrot=skrot, nazwa=nazwa)
        for klass in [Typ_KBN, Zrodlo_Informacji, Status_Korekty]:
            mommy.make(klass)

        super(TestCacheSimple, self).setUp()

    @with_cache
    def test_get_original_object(self):
        Rekord.objects.full_refresh()
        for model in self.wszystkie_modele:
            c = Rekord.objects.get_original(model)
            self.assertEqual(c.original, model)

    @with_cache
    def test_cache_triggers(self):
        T1 = "OMG ROXX"
        T2 = "LOL"

        for model in self.wszystkie_modele:
            model.tytul_oryginalny = T1
            model.save()
            self.assertEqual(Rekord.objects.get_original(model).tytul_oryginalny, T1)

            model.tytul_oryginalny = T2
            model.save()
            self.assertEqual(Rekord.objects.get_original(model).tytul_oryginalny, T2)

    def assertInstanceEquals(self, instance, values_dict):
        for key, value in list(values_dict.items()):
            instance_value = getattr(instance, key)
            self.assertEqual(
                instance_value,
                value,
                msg="key=%s, %s!=%s" % (key, value, instance_value),
            )

    @with_cache
    def test_tytul_sorted_version(self):
        for elem in [self.d, self.h, self.c, self.z]:  # self.p]:
            elem.tytul_oryginalny = "The 'APPROACH'"
            elem.jezyk = Jezyk.objects.get(skrot="ang.")
            elem.save()

            self.assertEqual(
                Rekord.objects.get_original(elem).tytul_oryginalny_sort, "approach"
            )

            elem.tytul_oryginalny = "le 'test'"
            elem.jezyk = Jezyk.objects.get(skrot="fr.")
            elem.save()

            # elem = elem.__class__.objects.get(pk=elem.pk) #reload
            # self.assertEquals(elem.tytul_oryginalny_sort, "test")

            self.assertEqual(
                Rekord.objects.get_original(elem).tytul_oryginalny_sort, "test"
            )


class TestCacheZapisani(LoadFixturesMixin, TestCase):
    fixtures = ["typ_odpowiedzialnosci.json"]

    def test_zapisani_wielu(self):
        aut = any_autor("Kowalski", "Jan")
        aut2 = any_autor("Nowak", "Jan")

        mommy.make(Uczelnia)
        jed = mommy.make(Jednostka)
        wyd = any_ciagle(tytul_oryginalny="Wydawnictwo ciagle")

        for kolejnosc, autor in enumerate([aut, aut2]):
            Wydawnictwo_Ciagle_Autor.objects.create(
                autor=autor,
                jednostka=jed,
                rekord=wyd,
                typ_odpowiedzialnosci_id=1,
                zapisany_jako="FOO BAR",
                kolejnosc=kolejnosc,
            )

        Rekord.objects.full_refresh()
        c = Rekord.objects.get_original(wyd)

        # Upewnij się, że w przypadku pracy z wieloma autorami do cache
        # zapisywane jest nie nazwisko z pól 'zapisany_jako' w bazie danych,
        # a oryginalne
        self.assertEqual(
            c.opis_bibliograficzny_autorzy_cache, ["Kowalski Jan", "Nowak Jan"]
        )

        # Upewnij się, że pole 'opis_bibliograficzny_zapisani_autorzy_cache'
        # zapisywane jest prawidłowo
        self.assertEqual(
            c.opis_bibliograficzny_zapisani_autorzy_cache, "FOO BAR, FOO BAR"
        )

    def test_zapisani_jeden(self):
        aut = any_autor("Kowalski", "Jan")
        mommy.make(Uczelnia)
        dok = mommy.make(Praca_Doktorska, tytul_oryginalny="Doktorat", autor=aut)

        Rekord.objects.full_refresh()
        c = Rekord.objects.get_original(dok)

        # Upewnij się, że w przypadku pracy z jednym autorem do cache
        # zapisywana jest prawidłowa wartość
        self.assertEqual(c.opis_bibliograficzny_autorzy_cache, ["Kowalski Jan"])

        self.assertEqual(c.opis_bibliograficzny_zapisani_autorzy_cache, "Kowalski Jan")


class TestMinimalCachingProblem(LoadFixturesMixin, TestCase):
    fixtures = ["status_korekty.json", "jezyk.json", "typ_odpowiedzialnosci.json"]

    @with_cache
    def test_tworzenie(self):
        self.j = mommy.make(Jednostka)
        self.a = any_autor()

        self.assertEqual(Autorzy.objects.all().count(), 0)

        c = any_ciagle(impact_factor=5, punktacja_wewnetrzna=0)
        self.assertEqual(Rekord.objects.all().count(), 1)

        c.dodaj_autora(self.a, self.j)

        self.assertEqual(AutorzyView.objects.all().count(), 1)
        self.assertEqual(Autorzy.objects.all().count(), 1)

    @with_cache
    def test_usuwanie(self):
        self.j = mommy.make(Jednostka)
        self.a = any_autor()

        self.assertEqual(Autorzy.objects.all().count(), 0)

        c = any_ciagle(impact_factor=5, punktacja_wewnetrzna=0)
        self.assertEqual(Rekord.objects.all().count(), 1)

        c.dodaj_autora(self.a, self.j)

        c.delete()

        self.assertEqual(AutorzyView.objects.all().count(), 0)
        self.assertEqual(Autorzy.objects.all().count(), 0)
