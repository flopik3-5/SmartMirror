from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtWidgets import QWidget
from source.UI.widgets.extensions import set_widget_background


class ResizeableText(QWidget):
    def __init__(self, text):
        super().__init__()
        self.text = text
        set_widget_background(self)

    def set_text(self, text):
        self.text = text
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont('Decorative', self.rect().height() * 0.6))
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)
