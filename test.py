from pynode_next import *

def test():
    
    for i in "ab":
        graph.add_node(i)
        #pause(23)
    
    graph.add_edge("a", "b")
    graph.add_edge("a", "b")
    pause(1000)

    graph.remove_edge("a", "b")
    graph.add_all([Node(i, i) for i in "zxy"])
    pause(100)
    graph.node("a").set_label("hi", label_id=1)    
    #graph.remove_edge(e)

#    core.ax(lambda x: x.dispatch({"attrs":{"edges":{"a-b-hihu":{}}}})

begin_pynode_next(test)
