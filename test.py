import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    for i in range(100):
        graph.add_node(i)
        
    pause(100)
    core.ax(lambda x: x.dispatch({"isPyNodeNext": True, "type": "alert", "message": 'hello, this is an alert sent via python.'}))

        
        

begin_pynode_next(test)
