from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QFont, QFontMetrics
from PyQt5.QtWidgets import QWidget

from source.UI.widgets.extensions import set_widget_background


class ResizeableText(QWidget):
    def __init__(self, text, alignment=QtCore.Qt.AlignCenter):
        super().__init__()
        self.text = text
        self.alignment = alignment
        set_widget_background(self)

    def set_text(self, text):
        self.text = text
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont('Decorative', self.get_font_size(self.rect())))
        painter.drawText(self.rect(), self.alignment | QtCore.Qt.AlignVCenter, self.text)

    def get_font_size(self, rect):
        for size in reversed(range(0, int(rect.height() * 0.65) + 1)):
            text_width = QFontMetrics(QFont('Decorative', size)).width(self.text)
            if text_width < rect.width():
                return size
