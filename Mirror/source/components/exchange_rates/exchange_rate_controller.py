class ExchangeRatesController:
    def __init__(self, parser):
        self.parser = __import__(f'source.components.exchange_rates.services.{parser}.{parser}',
                                 fromlist=['Parser']).Parser()

    def current_rates(self, currencies):
        return self.parser.current_rates(currencies)
