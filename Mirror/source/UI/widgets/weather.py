import os
import time
from threading import Thread
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout
from source.UI.widgets.extensions import set_widget_background
from source.UI.widgets.resizeable_image import ResizeableImage
from source.UI.widgets.resizeable_text import ResizeableText
from source.components.language.language import Language
from source.components.weather.weather_controller import WeatherController


class WeatherWidget(QWidget):
    time_to_update = pyqtSignal()

    def __init__(self):
        super().__init__()
        lang = Language()
        weather = WeatherController('yandex').current_weather('Минск')
        self.header_label = ResizeableText(f'{lang["now"]} {lang["in"]} {weather.city}: {weather.condition}')
        self.cloud_widget = ResizeableImage(f'{os.path.dirname(__file__)}\images\weather\{weather.image}')
        self.temperature_widget = ResizeableText(f'{weather.temperature}{lang["deg_m"]}')
        self.wind_label = ResizeableText(lang['wind'])
        self.wind_widget = ResizeableText(f'{weather.wind} {lang["wind_m"]}, {weather.wind_direction_abbr}')
        self.pressure_label = ResizeableText(lang['pressure'])
        self.pressure_widget = ResizeableText(f'{weather.pressure} {lang["pressure_m"]}')
        self.humidity_label = ResizeableText(lang['humidity'])
        self.humidity_widget = ResizeableText(f'{weather.humidity}{lang["humidity_m"]}')
        self.init_ui()
        self.init_threads()

    def init_ui(self):
        self.init_layout()
        self.setStyleSheet("ResizeableText {color: white}")
        set_widget_background(self)

    def init_layout(self):
        layout = QGridLayout()
        layout.addWidget(QWidget(), 0, 0, 1, 8)
        layout.addWidget(self.header_label, 1, 1, 1, 6)
        layout.addWidget(self.cloud_widget, 2, 1, 2, 2)
        layout.addWidget(self.temperature_widget, 2, 3, 2, 2)
        layout.addWidget(self.wind_label, 4, 1, 1, 2)
        layout.addWidget(self.wind_widget, 5, 1, 1, 2)
        layout.addWidget(self.pressure_label, 4, 3, 1, 2)
        layout.addWidget(self.pressure_widget, 5, 3, 1, 2)
        layout.addWidget(self.humidity_label, 4, 5, 1, 2)
        layout.addWidget(self.humidity_widget, 5, 5, 1, 2)
        layout.addWidget(QWidget(), 6, 0, 1, 8)
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
        lang = Language()
        weather = WeatherController('yandex').current_weather('Минск')
        self.header_label.set_text(f'{lang["now"]} {lang["in"]} {weather.city}: {weather.condition}')
        self.cloud_widget.set_image(f'{os.path.dirname(__file__)}\images\weather\{weather.image}')
        self.temperature_widget.set_text(f'{weather.temperature}{lang["deg_m"]}')
        self.wind_label.set_text(lang['wind'])
        self.wind_widget.set_text(f'{weather.wind} {lang["wind_m"]}, {weather.wind_direction_abbr}')
        self.pressure_label.set_text(lang['pressure'])
        self.pressure_widget.set_text(f'{weather.pressure} {lang["pressure_m"]}')
        self.humidity_label.set_text(lang['humidity'])
        self.humidity_widget.set_text(f'{weather.humidity}{lang["humidity_m"]}')
