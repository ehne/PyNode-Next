from pynode_next import *

def test():
    core.ax(lambda x: x.node("a").add())
    pause(1000)
    core.ax(lambda x: x.node("b").add())


begin_pynode_next(test)