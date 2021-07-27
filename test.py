from pynode_next import *

def test():
    print(core)
    core.ax(lambda a: a.node(1).add())

begin_pynode_next(test)