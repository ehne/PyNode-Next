import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *


def test():
    global z
    a = Node('a')
    b = Node('b')
    e = Edge('a', 'b').set_color(Color.RED)

    graph.add_all([a, b, e])
    z = 1
    def func():
        global z
        graph.add_node(z)
        z = z + 1
    
    t = delay(func, 1000, repeat=True)

    register_click_handler(lambda x: cancel_delay(t))
    

begin_pynode_next(test)
