from pynode_next import *

def test():
    
    for i in "abcd":
        graph.add_node(i)
        #pause(23)
    for ix, v in enumerate("xyz"):
        graph.nodes()[ix].set_value(v)

    
    [graph.node(i).set_color(Color.RED) for i in "ac"]

    for node in graph.nodes():
        for node2 in graph.nodes():
            graph.add_edge(node,node2)
            #pause(23)
    
    e = Node("q", "Object!")
    print(graph.node(e))
    graph.add_node(e)
    print(graph.node(e))
    print(graph.edges_between("a", "b"))

#    core.ax(lambda x: x.dispatch({"attrs":{"edges":{"a-b-hihu":{}}}})

begin_pynode_next(test)
