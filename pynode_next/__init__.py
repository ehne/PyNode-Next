from .color import *
from .node import *
from .core import core


class Edge:
    pass
 

def begin_pynode_next(func):
    core.run(func)
