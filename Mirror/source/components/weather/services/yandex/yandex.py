import jsonpickle
import os

from pip._vendor import requests
from pyquery import PyQuery

from source.components.weather.weather import Weather


class Parser:
    def __init__(self):
        self.file = jsonpickle.decode(open(f'{os.path.dirname(__file__)}\yandex.json', 'r').read())

    def current_weather(self, city):
        page = PyQuery(self.search_city(city))
        return Weather(
            self.weather_image(PyQuery(page)('.fact .fact__condition').text().lower()),
            PyQuery(page)('.location .title_level_1').text().split(' ')[2],
            PyQuery(page)('.fact .fact__temp .temp__value').text().replace('−', '-'),
            PyQuery(page)('.fact .fact__condition').text(),
            PyQuery(page)('.fact .wind-speed').text(),
            PyQuery(page)('.fact .fact__wind-speed .fact__unit abbr').attr('title').split(' ')[1],
            PyQuery(page)('.fact .fact__wind-speed .fact__unit abbr').text(),
            PyQuery(page)('.fact .fact__pressure .term__value').children().remove().end().text(),
            PyQuery(page)('.fact .fact__humidity .term__value').text()[:-1])

    def weather_image(self, condition):
        return self.file[condition]

    @staticmethod
    def search_city(name):
        page = requests.get(f'https://yandex.by/pogoda/search?request={name}').text
        return 'https://yandex.by' + PyQuery(page)('.link.place-list__item-name').attr('href')
