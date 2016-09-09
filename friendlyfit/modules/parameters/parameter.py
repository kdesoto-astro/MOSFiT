from ..module import Module

CLASS_NAME = 'Parameter'


class Parameter(Module):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._max_value = kwargs.get('max_value', None)
        self._min_value = kwargs.get('min_value', None)
        self._log = kwargs.get('log', False)

    def process(self, **kwargs):
        value = (kwargs['fraction'] *
                 (self._max_value - self._min_value) + self._min_value)
        return {'value': value}
