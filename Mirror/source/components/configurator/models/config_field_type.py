from enum import Enum


class ConfigFieldType(Enum):
    menu = 0
    text = 1
    time = 2
    date = 3
    dropdown = 4
    checkbox = 5

    def __getstate__(self):
        return self._value_
