from random import randint, seed
from PyQt5.QtGui import QColor

show_widget_borders = False


def set_widget_background(widget, r=None, g=None, b=None):
    if r is None or g is None or b is None:
        if show_widget_borders:
            seed(randint(0, 255))
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
        else:
            return
    widget.setAutoFillBackground(True)
    palette = widget.palette()
    palette.setColor(widget.backgroundRole(), QColor(r, g, b))
    widget.setPalette(palette)
