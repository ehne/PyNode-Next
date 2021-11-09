import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import pynode_next


def test():
    graph.add_node('a', None)
    
    graph.add_node('b', 'hello')

    graph.add_edge('a', 'b', directed=True)
    

begin_pynode_next(test)
