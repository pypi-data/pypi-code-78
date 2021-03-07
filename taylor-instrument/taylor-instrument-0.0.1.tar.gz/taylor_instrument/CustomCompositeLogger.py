# -*- coding: utf-8 -*-

from pip_services3_components.log import CompositeLogger


class CustomCompositeLogger(CompositeLogger):
    _correlation_id = None

    def configure(self, config):
        self._correlation_id = config.get_as_nullable_string("correlation_id")
        super().configure(config)

    def log(self, level, error, message, correlation_id=None, *args, **kwargs):
        super().log(level, correlation_id or self._correlation_id, error, message, *args, **kwargs)

    def fatal(self, error, message, correlation_id=None, *args, **kwargs):
        super().fatal(correlation_id or self._correlation_id, error, message, *args, **kwargs)

    def error(self, error, message, correlation_id=None, *args, **kwargs):
        super().error(correlation_id or self._correlation_id, error, message, *args, **kwargs)

    def warn(self, message, correlation_id=None, *args, **kwargs):
        super().warn(correlation_id or self._correlation_id, message, *args, **kwargs)

    def info(self, message, correlation_id=None, *args, **kwargs):
        super().info(correlation_id or self._correlation_id, message, *args, **kwargs)

    def debug(self, message, correlation_id=None, *args, **kwargs):
        super().debug(correlation_id or self._correlation_id, message, *args, **kwargs)

    def trace(self, message, correlation_id=None, *args, **kwargs):
        super().trace(correlation_id or self._correlation_id, message, *args, **kwargs)
