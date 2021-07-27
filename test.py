from pynode_next import *

def test():
    
    graph.add_node("a")
    graph.add_node("b")
   # graph.add_node("a")
    e = graph.add_edge("a", "b", directed=True)
    print(graph.node("a").outgoing_edges())

begin_pynode_next(test)