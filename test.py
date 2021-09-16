import inspect
from typing import Iterable, List, Union, get_args
from pynode_next import *
import random

def test():
    graph.add_node("(0, 0)").set_position(0, 0)
    graph.add_node("(1, 1)").set_position(1, 1)

begin_pynode_next(test)
