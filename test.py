import inspect
from typing import Iterable, List, Union, get_args
from pynode_next import *
import random

def test():
    graph.add_node("a", "Room A\n(wumpus)")
    graph.add_node("b", "Maps\nGoogle.com")
    pause(500)
    graph.add_edge("a", "b")
    register_click_handler(lambda x: print(x._data()))
    

begin_pynode_next(test)
