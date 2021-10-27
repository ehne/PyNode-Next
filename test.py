import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    graph.add_node("a").set_value('1')
    n = Node('b').set_value('2').set_size(50)
    pause(1000)
    graph.add_node(n)
    
begin_pynode_next(test)
