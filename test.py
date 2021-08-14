from pynode_next import *
import random

def test():
    g = graph.random(4, 3)
    print(g)
    ##graph.remove_edge(e)
    #print([str(i) for i in graph.node("a").adjacent_nodes()])
    pause(500)
    graph.add_all(g)
begin_pynode_next(test)
