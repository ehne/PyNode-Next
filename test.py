import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *


def test():
    a = graph.add_node('a')
    a.set_color(Color.from_hex_int(0x0055ff))
    graph.add_node('b')
    graph.add_edge('a', 'b').set_width(40)

    print(graph.has_node(a))
    print(graph.has_node(Node("c")))
begin_pynode_next(test)
