import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import pynode_next


def test():
    graph.add_node('a', None)
    
    b = graph.add_node('b', 'hello')

    e = graph.add_edge('a', 'b', directed=True)

    print(graph.node('a'))
    print(graph.node(b))

    pause(1000)

    graph.remove(b)

begin_pynode_next(test)
