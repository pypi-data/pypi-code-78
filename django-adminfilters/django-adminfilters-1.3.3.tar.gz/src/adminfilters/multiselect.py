from django.contrib.admin.filters import FieldListFilter
from django.db.models.fields import AutoField, IntegerField
from django.utils.translation import ugettext_lazy as _


class MultipleSelectFieldListFilter(FieldListFilter):

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s_filter' % field_path
        self.filter_statement = '%s' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        self.lookup_choices = field.get_choices(include_blank=False)
        super(MultipleSelectFieldListFilter, self).__init__(
            field, request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def get_field(self):
        try:
            field = self.field.remote_field.model._meta.pk
        except AttributeError:  # django < 2.0
            field = self.field.rel.to._meta.pk
        return field

    def values(self):
        """
        Returns a list of values to filter on.
        """
        values = []
        value = self.used_parameters.get(self.lookup_kwarg, None)
        if value:
            values = value.split(',')

        field = self.get_field()
        # convert to integers if IntegerField
        if type(field) in [IntegerField, AutoField]:
            values = [int(x) for x in values]
        return values

    def queryset(self, request, queryset):
        raise NotImplementedError

    def choices(self, cl):
        # from django.contrib.admin.views.main import EMPTY_CHANGELIST_VALUE
        yield {
            'selected': self.lookup_val is None,
            'query_string': cl.get_query_string(
                {},
                [self.lookup_kwarg]),
            'display': _('All')
        }
        for pk_val, val in self.lookup_choices:
            selected = pk_val in self.values()
            pk_list = set(self.values())
            if selected:
                pk_list.remove(pk_val)
            else:
                pk_list.add(pk_val)
            queryset_value = ','.join([str(x) for x in pk_list])
            if pk_list:
                query_string = cl.get_query_string(
                    {
                        self.lookup_kwarg: queryset_value,
                    })
            else:
                query_string = cl.get_query_string({}, [self.lookup_kwarg])
            yield {
                'selected': selected,
                'query_string': query_string,
                'display': val,
            }


class IntersectionFieldListFilter(MultipleSelectFieldListFilter):
    """
    A FieldListFilter which allows multiple selection of
    filters for many-to-many type fields. A list of objects will be
    returned whose m2m contains all the selected filters.
    """

    def queryset(self, request, queryset):
        for value in self.values():
            filter_dct = {
                self.filter_statement: value
            }
            queryset = queryset.filter(**filter_dct)
        return queryset


class UnionFieldListFilter(MultipleSelectFieldListFilter):
    """
    A FieldListFilter which allows multiple selection of
    filters for many-to-many type fields, or any type with choices.
    A list of objects will be returned whose m2m or value set
    contains one of the selected filters.
    """

    def get_field(self):
        try:
            field = super(UnionFieldListFilter, self).get_field()
        except AttributeError:
            if hasattr(self.field, "choices") and self.field.choices:
                field = self.field  # It's a *Field with choises
            else:
                raise AttributeError(
                    'Multiselect field must be a FK or any type with choices')
        return field

    def queryset(self, request, queryset):
        filter_statement = "%s__in" % self.filter_statement
        filter_values = self.values()
        filter_dct = {
            filter_statement: filter_values
        }
        if filter_values:
            return queryset.filter(**filter_dct)
        else:
            return queryset
