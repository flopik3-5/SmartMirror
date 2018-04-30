from PyQt5 import QtCore
from threading import Thread

import time
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout

from source.UI.widgets.extensions import set_widget_background
from source.UI.widgets.resizeable_text import ResizeableText
from source.components.language.language import Language
from source.components.news.news_controller import NewsController


class NewsWidget(QWidget):
    time_to_update = pyqtSignal()

    def __init__(self):
        super().__init__()
        lang = Language()
        self.news = NewsController('tutby').current_news("top")
        self.header_label = ResizeableText(
            f'{lang["news"]} {"(" + self.news[0] + ")" if self.news[0] is not None else " "}',
            QtCore.Qt.AlignLeft)
        self.news_labels = [ResizeableText("", QtCore.Qt.AlignLeft) for i in range(0, 8)]
        for i in range(0, self.news[1].__len__()):
            self.news_labels[i].set_text(self.news[1][i].title)
        self.init_ui()
        self.init_threads()

    def init_ui(self):
        self.init_layout()
        self.setStyleSheet("ResizeableText {color: white}")
        set_widget_background(self)

    def init_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.header_label, 0, 0, 1, 1)
        for i in range(0, self.news_labels.__len__()):
            layout.addWidget(self.news_labels[i], 1 + i, 0, 1, 1)
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
        self.news = NewsController('tutby').current_news("top")
        self.header_label.set_text(f'{lang["news"]} {"(" + self.news[0] + ")" if self.news[0] is not None else " "}')
        for i in range(0, self.news[1].__len__()):
            self.news_labels[i].set_text(self.news[1][i].title)
