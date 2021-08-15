import inspect
from typing import Iterable, List, Union, get_args, _UnionGenericAlias
from pynode_next import *
import random

def test():
    graph.add_node("1")
    graph.add_node(2)
    graph.add_edge("1", 2)

    print(graph.node(1))

begin_pynode_next(test)
