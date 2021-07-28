from pynode_next import *

def test():
    
    for i in "abcd":
        graph.add_node(i)
        #pause(23)
    
    e = graph.add_edge("a", "b")

    pause(1000)

    graph.remove_edge(e)

#    core.ax(lambda x: x.dispatch({"attrs":{"edges":{"a-b-hihu":{}}}})

begin_pynode_next(test)
