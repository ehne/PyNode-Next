from .misc import *
from .node import *
from .errors import *
from .edge import *
from .core import core
from .graph import graph

def begin_pynode_next(func):
    core.run(func)
