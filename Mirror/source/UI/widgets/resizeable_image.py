from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtWidgets import QWidget
from source.UI.widgets.extensions import set_widget_background


class ResizeableImage(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QImage(image_path)
        set_widget_background(self)

    def set_image(self, image_path):
        self.image = QImage(image_path)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        size = min(self.rect().height(), self.rect().width())
        x = (self.rect().width() - size) / 2
        y = (self.rect().height() - size) / 2
        painter.drawImage(QRect(x, y, size, size), self.image)
