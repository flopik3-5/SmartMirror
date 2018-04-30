from PyQt5.QtWidgets import QWidget, QGridLayout

from source.UI.widgets.clock import ClockWidget
from source.UI.widgets.exchange_rates import ExchangeRatesWidget
from source.UI.widgets.extensions import set_widget_background
from source.UI.widgets.news import NewsWidget
from source.UI.widgets.weather import WeatherWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        set_widget_background(self, 0, 0, 0)
        self.init_layout()
        self.showFullScreen()

    def init_layout(self):
        layout = QGridLayout()
        layout.addWidget(ClockWidget(), 0, 0, 4, 4)
        layout.addWidget(WeatherWidget(), 0, 4, 4, 4)
        layout.addWidget(ExchangeRatesWidget(), 0, 8, 4, 2)
        layout.addWidget(QWidget(), 4, 0, 2, 10)
        layout.addWidget(QWidget(), 6, 0, 2, 10)
        layout.addWidget(QWidget(), 8, 0, 2, 10)
        layout.addWidget(NewsWidget(), 10, 0, 4, 5)
        layout.addWidget(QWidget(), 10, 5, 4, 5)
        self.setLayout(layout)
