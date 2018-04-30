import os
import time
from threading import Thread

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout

from source.UI.widgets.extensions import set_widget_background
from source.UI.widgets.resizeable_image import ResizeableImage
from source.UI.widgets.resizeable_text import ResizeableText
from source.components.exchange_rates.exchange_rate_controller import ExchangeRatesController
from source.components.language.language import Language


class ExchangeRatesWidget(QWidget):
    time_to_update = pyqtSignal()

    def __init__(self):
        super().__init__()
        lang = Language()
        self.header_label = ResizeableText(lang["exchange_rates"])
        self.rates = ExchangeRatesController("nbrb").current_rates([290, 145, 292])
        self.rate_rows = [[ResizeableText(rate.scale), ResizeableText(rate.currency_abbr),
                           ResizeableImage(f'{os.path.dirname(__file__)}\images\exchange_rates\\arrows.png'),
                           ResizeableText(rate.rate), ResizeableText(rate.main_currency_abbr)] for rate in self.rates]
        self.init_ui()
        self.init_threads()

    def init_ui(self):
        self.init_layout()
        self.setStyleSheet("ResizeableText {color: white}")
        set_widget_background(self)

    def init_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.header_label, 0, 0, 1, 5)
        for i in range(0, self.rate_rows.__len__()):
            for j in range(0, self.rate_rows[i].__len__()):
                layout.addWidget(self.rate_rows[i][j], 1 + i, j, 1, 1)
        self.setLayout(layout)

    def init_threads(self):
        self.time_to_update.connect(self.update)
        Thread(target=self.clock, daemon=True).start()

    def clock(self):
        while True:
            time.sleep(900)
            self.time_to_update.emit()

    @pyqtSlot()
    def update(self):
        self.rates = ExchangeRatesController("nbrb").current_rates([290, 145, 292])
        for i in range(0, self.rates.__len__()):
            self.rate_rows[i][0].set_text(self.rates[i].scale)
            self.rate_rows[i][1].set_text(self.rates[i].currency_abbr)
            self.rate_rows[i][3].set_text(self.rates[i].rate)
            self.rate_rows[i][4].set_text(self.rates[i].main_currency_name)
