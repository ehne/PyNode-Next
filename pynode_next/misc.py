from threading import Timer as ThreadingTimer
import uuid
from .core import core

class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
        
    def hex_string(self):
        return "#%02x%02x%02x" % (self._red, self._green, self._blue)

    def __str__(self):
        return self.hex_string()

Color.RED = Color(180, 0, 0)
Color.GREEN = Color(0, 150, 0)
Color.BLUE = Color(0, 0, 200)
Color.YELLOW = Color(255, 215, 0)
Color.WHITE = Color(255, 255, 255)
Color.LIGHT_GREY = Color(179, 179, 179)
Color.GREY = Color(102, 102, 102)
Color.DARK_GREY = Color(26, 26, 26)
Color.BLACK = Color(0, 0, 0)

def pause(pause_time):
    core.ax(lambda x: x.pause(pause_time * 0.001))

# delay stuff:

__intervals = {}

def delay(func, time, args=[], repeat=False):
    """Executes the given function after the specified number of miliseconds with the optional arguments. If repeat is set the function will run again until the delay is cancelled. Returns the delay id"""
    new_func = lambda: func(*args)
    t_id = str(uuid.uuid4())

    if not repeat:
        # set up the timer to execute once
        t = ThreadingTimer(time / 1000.0, new_func)
        __intervals[t_id] = t
        t.start()
    else:
        # set up the timer to execute many times
        def loop_func(timer_id, func_to_loop, time):
            t = ThreadingTimer(time / 1000.0, loop_func, (timer_id, func_to_loop, time))
            __intervals[timer_id] = t
            t.start()
            func_to_loop()
        loop_func(t_id, new_func, time)

    return t_id

def cancel_delay(delay_id):
    """Cancels the given delay."""
    __intervals[delay_id].cancel()

def alert(message: str):
    core.ax(lambda x: x.dispatch({"isPyNodeNext": True, "type": "alert", "message": message}))