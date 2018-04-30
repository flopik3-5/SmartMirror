class WeatherController:
    def __init__(self, parser):
        self.parser = __import__(f'source.components.weather.services.{parser}.{parser}', fromlist=['Parser']).Parser()

    def current_weather(self, city):
        return self.parser.current_weather(city)
