import os
import time
from datetime import datetime
from threading import Thread
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout
from source.UI.widgets.resizeable_text import ResizeableText
from source.UI.widgets.extensions import set_widget_background
from source.UI.widgets.resizeable_image import ResizeableImage


class ClockWidget(QWidget):
    time_refreshed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.sun_widget = ResizeableImage(f'{os.path.dirname(__file__)}\images\clock\{self.current_time_image()}.png')
        self.time_widget = ResizeableText(datetime.now().strftime("%H:%M"))
        self.date_widget = ResizeableText(datetime.now().strftime("%d %B %Y"))
        self.init_ui()
        self.init_threads()

    def init_ui(self):
        self.init_layout()
        self.setStyleSheet("ResizeableText {color: white}")
        set_widget_background(self)

    def init_layout(self):
        layout = QGridLayout()
        layout.addWidget(QWidget(), 0, 0, 1, 6)
        layout.addWidget(self.sun_widget, 1, 1, 2, 1)
        layout.addWidget(self.time_widget, 1, 2, 2, 3)
        layout.addWidget(self.date_widget, 3, 1, 1, 4)
        layout.addWidget(QWidget(), 4, 0, 1, 6)
        self.setLayout(layout)

    def init_threads(self):
        self.time_refreshed.connect(self.time_refresh)
        Thread(target=self.clock, daemon=True).start()

    def clock(self):
        m = datetime.now().minute
        while True:
            time.sleep(1)
            if m != datetime.now().minute:
                m = datetime.now().minute
                self.time_refreshed.emit()

    @pyqtSlot()
    def time_refresh(self):
        self.time_widget.set_text(datetime.now().strftime("%H:%M"))
        self.date_widget.set_text(datetime.now().strftime("%d %B %Y"))
        self.sun_widget.set_image(f'{os.path.dirname(__file__)}\images\clock\{self.current_time_image()}.png')

    @staticmethod
    def current_time_image():
        h = datetime.now().hour
        return h if (h % 2 == 0) else h - 1
