import locale
import jsonpickle
import os


class Language:
    def __init__(self):
        self.file = jsonpickle.decode(open(f'{os.path.dirname(__file__)}\lang\{locale.getlocale()[0]}.json', 'r').read())

    def __getitem__(self, item):
        return self.file[item]
