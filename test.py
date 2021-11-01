import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *


def test():
    a = graph.add_node('a')
    a.set_position(0,0)

begin_pynode_next(test)
