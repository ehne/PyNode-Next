from .core import core

class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
        
    def hex_string(self):
        return "#%02x%02x%02x" % (self._red, self._green, self._blue)

Color.RED = Color(180, 0, 0)
Color.GREEN = Color(0, 150, 0)
Color.BLUE = Color(0, 0, 200)
Color.YELLOW = Color(255, 215, 0)
Color.WHITE = Color(255, 255, 255)
Color.LIGHT_GREY = Color(199, 199, 199)
Color.GREY = Color(127, 127, 127)
Color.DARK_GREY = Color(82, 82, 82)
Color.BLACK = Color(0, 0, 0)

def pause(pause_time):
    core.ax(lambda x: x.pause(pause_time * 0.001))