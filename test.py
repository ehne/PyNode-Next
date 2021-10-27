import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    graph.add_node("a")
    graph.add_node("b").set_size(50)
    graph.node('b').set_label('top right').set_label('top left', 1)
    
begin_pynode_next(test)
