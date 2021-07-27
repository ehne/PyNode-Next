from .color import *
from .node import *
from .core import core


class Edge:
    pass
 
class Graph:
    def __init__(self):
        self._nodes = {}
        self._edges = []

graph = Graph()

def begin_pynode_next(func):
    core.run(func)
