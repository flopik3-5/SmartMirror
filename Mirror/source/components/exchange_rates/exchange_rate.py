from source.components.language.language import Language


class ExchangeRate:
    def __init__(self, main_currency_abbr, main_currency_name, currency_abbr, currency_name, scale, rate):
        self.main_currency_abbr = main_currency_abbr
        self.main_currency_name = main_currency_name
        self.currency_abbr = currency_abbr
        self.currency_name = currency_name
        self.scale = str(scale)
        self.rate = str(rate)

    def __str__(self):
        lang = Language()
        return f'{self.scale} {self.currency_name} {lang["to"]} {self.rate} {self.main_currency_name}'
