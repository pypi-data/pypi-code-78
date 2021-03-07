import os

import django

from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "django_logger"))


def boot_django():
    settings.configure(
        DJANGO_LOGGER_APPLICATION="DJANGO LOGGER",
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "../db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
            "django_logger",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )

    django.setup()
