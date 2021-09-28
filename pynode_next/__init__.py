import webbrowser
from .misc import *
from .node import *
from .errors import *
from .edge import *
from .core import core
from .graph import graph, register_click_handler

def begin_pynode_next(func, open_browser=True):
    if open_browser:
        webbrowser.open(f"http://localhost:{core.port}")
    def new_func():
        graph.clear()
        func()
    core.run(new_func)
