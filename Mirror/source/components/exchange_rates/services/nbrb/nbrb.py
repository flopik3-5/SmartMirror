import jsonpickle
from source.components.exchange_rates.exchange_rate import ExchangeRate
from source.components.language.language import Language
import requests


class Parser:
    def __init__(self):
        self.rates = jsonpickle.decode(requests.get("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0").text)
        self.currencies_url = "http://www.nbrb.by/API/ExRates/Currencies/"

    def current_rates(self, currencies):
        selected_currencies = list(filter(lambda x: x["Cur_ID"] in currencies, self.rates))
        exchange_rates = []
        lang = Language()
        for selected_currency in selected_currencies:
            exchange_rates.append(ExchangeRate("BYN", lang["byn_r_p"], selected_currency["Cur_Abbreviation"],
                                               selected_currency["Cur_Name"], selected_currency["Cur_Scale"],
                                               selected_currency["Cur_OfficialRate"]))
        return exchange_rates
