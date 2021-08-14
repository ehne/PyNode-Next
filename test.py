from pynode_next import *

def test():
    
    for i in "ab":
        graph.add_node(i)
    e = Edge("a", "b")
    graph.add_edge(e)
    pause(500)
    e.set_weight(100)
    e.set_weight_style(color=Color.RED)
    core.ax(lambda x: x.nodes("cd").add())
    core.ax(lambda x: x.edge("cd").add())
    pause(500)
    core.ax(lambda x: x.edge("cd").highlight().color("#fa0"))
    pause(500)
    e.highlight(color=Color.GREEN)
    ##graph.remove_edge(e)
    print([str(i) for i in graph.node("a").adjacent_nodes()])

begin_pynode_next(test)
