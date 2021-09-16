import inspect
from typing import Iterable, List, Union, get_args
from pynode_next import *
import random

def test():
    graph.add_node("a")
    register_click_handler(lambda x: print(x._data()))
    

begin_pynode_next(test)
