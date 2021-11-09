from pynode_next import *
import time


def test():
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a', 'b', 'hello!')

begin_pynode_next(test)
