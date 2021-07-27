from pynode_next import *

def test():
    graph.add_node("a", value="huh")
    
    pause(1000)
    
    print(graph.node("a"))

    graph.node("a").set_value("hi")
    print(graph.nodes())
    graph.add_node("a")


begin_pynode_next(test)