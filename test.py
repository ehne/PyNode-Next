from pynode_next import *

def test():
    graph.add_node("a", value="huh")
        
    graph.add_node("b")

    graph.node("a").set_value("hi")
    print(graph.nodes())
    


begin_pynode_next(test)