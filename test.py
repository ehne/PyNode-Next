import inspect
from sys import excepthook
from types import DynamicClassAttribute
from typing import Iterable, List, Union, final, get_args
from pynode_next import *
import random


def test():
    for i in range(100):
        graph.add_node(i)
        pause(24)
        
    def click(node):
        core.ax(lambda x: x.dispatch({"isPyNodeNext": True, "type": "alert", "message": f'You have selected node {node}'}))
        node.set_color(Color.RED)
    
    register_click_handler(click)

        
        

begin_pynode_next(test)
