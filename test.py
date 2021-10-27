import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    graph.add_node("a").set_value('1')
    
begin_pynode_next(test)
