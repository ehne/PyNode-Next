import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *


def test():
    a = Node('a')
    a.set_position(0.5, 0.75)
    print(a._data())
    graph.add_node(a)

begin_pynode_next(test)
