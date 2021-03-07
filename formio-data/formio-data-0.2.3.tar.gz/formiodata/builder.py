# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

import json
import logging
import uuid

from copy import deepcopy

from formiodata import components


class Builder:

    def __init__(self, schema_json, **kwargs):
        """
        @param schema_json
        @param lang
        """
        if isinstance(schema_json, dict):
            self.schema = schema_json
        else:
            self.schema = json.loads(schema_json)

        self.language = kwargs.get('language', 'en')
        # i18n (translations)
        self.i18n = kwargs.get('i18n', {})
        self.resources = kwargs.get('resources', {})

        # Raw components from the schema
        self._raw_components = []

        # Raw components enriched with Component(object) API.
        self.raw_components = []

        # Key/value dictionay of all components for instant access.
        self.components = {}
        self.component_ids = {}

        # Key/value dictionay of Form components for instant access.
        self.form_components = {}

        # Set/load component attrs intialized above.
        self.load_components()

        # TODO kwargs['component_cls']
        # Custom component classes
        self._component_cls = []

    def load_components(self):
        self._raw_components = self.schema.get('components')
        self.raw_components = deepcopy(self.schema.get('components'))
        if self.raw_components:
            self._load_components(self.raw_components)

    def _load_components(self, components, parent=None):
        """
        @param components
        """
        for component in components:
            # Only determine and load class if component type.
            if 'type' in component:
                component_obj = self.get_component_object(component)
                component_obj.load(None, None)
                self.component_ids[component_obj.id] = component_obj

                if parent:
                    component_obj.parent = parent

                component_obj.id = component.get('id', str(uuid.uuid4()))
                self.component_ids[component_obj.id] = component_obj
                component['_object'] = component_obj
                if component.get('key') and component.get('input'):
                    self.form_components[component.get('key')] = component_obj
                    self.components[component.get('key')] = component_obj
                else:
                    if component.get('key'):
                        key = component.get('key')
                    elif self.components.get(component.get('type')):
                        key = component.get('type') + '_x'
                    else:
                        key = component.get('type')
                    self.components[key] = component_obj

                # (Input) nested components (e.g. datagrid, editgrid)
                if component.get('components'):
                    self._load_components(component.get('components'), component_obj)

                # (Layout) nested components (e.g. columns, panels)
                for k, vals in component.copy().items():
                    if isinstance(vals, list):
                        for v in vals:
                            if 'components' in v:
                                self._load_components(v.get('components'), component_obj)
                            elif isinstance(v, list):
                                for sub_v in v:
                                    if 'components' in sub_v:
                                        self._load_components(sub_v.get('components'), component_obj)

    def get_component_object(self, component):
        """
        @param component
        """
        component_type = component.get('type')
        if component_type:
            try:
                cls_name = '%sComponent' % component_type
                cls = getattr(components, cls_name)
                component_obj = cls(component, self, language=self.language, i18n=self.i18n, resources=self.resources)
                return component_obj
            except AttributeError as e:
                # TODO try to find/load first from self._component_cls else
                # re-raise exception or silence (log error and return False)
                logging.error(e)
                # TODO: implement property (by kwargs) whether to return
                # (raw) Component object or throw exception,
                return components.Component(component, self)
        else:
            return False
