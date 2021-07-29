from pynode_next import *

def test():
    
    for i in "abcd":
        graph.add_node(i)
        pause(23)
    for i in graph.nodes():
        for j in graph.nodes():
            graph.add_edge(i, j,None, directed=True)
            pause(23)
    pause(1000)
    for i in graph._edges:
        i.traverse(keep_path=False)
        pause(100)
    #core.ax(lambda x: x.edge("ab").traverse(color="green"))
    ##graph.remove_edge(e)
    print([str(i) for i in graph.node("a").adjacent_nodes()])
#    core.ax(lambda x: x.dispatch({"attrs":{"edges":{"a-b-hihu":{}}}})

begin_pynode_next(test, open_browser=False)
