from pynode_next import *

def test():
    graph.add_node("a")
    graph.add_node("b")
    
    e = graph.add_edge("a", "b", directed=True)
    graph.add_edge(e)

begin_pynode_next(test)