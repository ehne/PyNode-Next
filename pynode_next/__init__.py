from .misc import *
from .node import *
from .errors import *
from .core import core

class Graph:
    def __init__(self):
        self._nodes = {}
        self._edges = []

    def add_node(self, *args, **kwargs):
        """Adds the node to the graph. Can be either the id/value combination or can be a Node object."""
        # figure out what has been given to the function
        if "node" in kwargs:
            n = kwargs["node"]
        elif len(args) > 0 and isinstance(args[0], Node):
            n = args[0]
        else:
            n = Node(*args, **kwargs)

        # Make sure there aren't two nodes with the same id
        if n._id in self._nodes:
            raise DuplicateNodeError(f"Duplicate node '{n._id}'")

        # add node to dict and canvas
        self._nodes[n._id] = n
        core.ax(lambda x: x.node(n._id).add(labels={0: {"text": n._value}}))

        return n

    def node(self, id):
        """Returns the node with the id specified."""
        if isinstance(id, Node) and id._id in self._nodes:
            return id
        elif id in self._nodes:
            return self._nodes[id]
        else:
            return None

    def nodes(self):
        """Returns all of the graph's nodes."""
        return list(self._nodes.values())

graph = Graph()


def begin_pynode_next(func):
    core.run(func)
