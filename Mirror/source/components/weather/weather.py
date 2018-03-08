from source.components.language.language import Language


class Weather:
    def __init__(self, image, city, temperature, condition, wind, wind_direction, wind_direction_abbr, pressure,
                 humidity):
        self.image = image
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.wind = wind
        self.wind_direction = wind_direction
        self.wind_direction_abbr = wind_direction_abbr
        self.pressure = pressure
        self.humidity = humidity

    def __str__(self):
        lang = Language()
        return f'{lang["in"]} {self.city} {self.temperature}{lang["deg_m"]}, {self.condition}. ' \
               f'{lang["wind"]} {self.wind} {lang["wind_m"]}, {self.wind_direction}. ' \
               f'{lang["pressure"]} {self.pressure} {lang["pressure_m"]}. ' \
               f'{lang["humidity"]} {self.humidity} {lang["humidity_m"]}.'
