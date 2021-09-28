import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    graph.add_node("a")
    graph.add_node("b")
    pause(500)
    graph.add_edge("a", "b")
    register_click_handler(lambda x: x.set_color(Color.GREEN))
    
begin_pynode_next(test)
