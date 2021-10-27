import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    a = Node('a')
    b = Node('b')
    e = Edge('a', 'b').set_color(Color.RED)

    graph.add_all([a, b, e])

begin_pynode_next(test)
