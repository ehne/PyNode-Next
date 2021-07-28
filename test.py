from pynode_next import *

def test():
    
    for i in "abcd":
        graph.add_node(Node("a", "b"))
        #pause(23)
    for ix, v in enumerate("xyz"):
        graph.nodes()[ix].set_value(v)

    
    [graph.node(i).set_color(Color.RED) for i in "ac"]

    for node in graph.nodes():
        for node2 in graph.nodes():
            graph.add_edge(node,node2)
            #pause(23)
    
    e = Node("q", "Object!")
    
    graph.add_node(e)
        
#    core.ax(lambda x: x.dispatch({"attrs":{"edges":{"a-b-hihu":{}}}})

begin_pynode_next(test)
