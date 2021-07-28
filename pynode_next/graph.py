from typing import Union
from .overloading import *

from .misc import *
from .node import *
from .errors import *
from .edge import *
from .core import core


class Graph:
    def __init__(self):
        self._nodes = {}
        self._edges = []
        self._has_edge_cache = {}

    @overloaded
    def add_node(self, id: str):
        """Adds a node to the graph using an id."""
        self.add_node(id, id)

    @overloads(add_node)
    def add_node(self, id: str, value: str):
        """Adds a node to the graph using an id and a value."""
        if value == None:
            value = id
        self.add_node(Node(id, value))

    @overloads(add_node)
    def add_node(self, node: Node):
        """Adds the node object to the graph."""
        # Make sure there aren't two nodes with the same id
        if node._id in self._nodes:
            raise DuplicateNodeError(f"Duplicate node with id '{node._id}'")

        # add node to dict and canvas
        self._nodes[node._id] = node
        # just sends all of the node's data
        core.ax(lambda x: x.dispatch(node._data()))
        return node

    def remove_node(self, node):
        pass

    @overloaded
    def node(self, id: str):
        """Returns the node with the id specified."""
        if id in self._nodes:
            return self._nodes[id]
        else:
            return None

    @overloads(node)
    def node(self, node: Node):
        if node._id in self._nodes:
            return node
        return None

    def nodes(self):
        """Returns all of the graph's nodes."""
        return list(self._nodes.values())

    @overloaded
    def add_edge(self, source: Node, target: Node, weight=None, directed: bool = False):
        """Adds an edge by defining it's relation to other nodes."""
        self.add_edge(Edge(source, target, weight, directed))

    @overloads(add_edge)
    def add_edge(self, edge: Edge):
        """Add an edge object to the graph."""
        e = edge
        if self.has_edge(e):
            raise DuplicateEdgeError(
                f"There is already an instance of the edge '{e}' in the graph"
            )

        # saves the original sources so we can check if they actually exist in the graph
        original_source = e._source
        original_target = e._target

        # incase the nodes were provided as node ids rather than objects.
        e._source = self.node(e._source)
        e._target = self.node(e._target)

        # Makes sure that the source and target nodes are actually in the graph
        if e._source == None:
            raise NodeDoesntExistError(
                f"The node {original_source} does not exist in the graph"
            )
        if e._target == None:
            raise NodeDoesntExistError(
                f"The node {original_target} does not exist in the graph"
            )

        # adds the incident edges to the nodes
        e._source._incident_edges.append(e)
        e._target._incident_edges.append(e)

        self._edges.append(e)
        self._has_edge_cache[e] = True

        # TODO: below should just dispatch the edge's data so that add_edge(Edge()) is fully supported
        core.ax(lambda x: x.dispatch(e._data()))
        return e

    def remove_edge(self, *args, **kwargs):
        removing_multiple = False
        # stuff for if provided an Edge object.
        if "edge" in kwargs:
            e = kwargs["edge"]
        elif len(args) > 0 and isinstance(args[0], Edge):
            e = args[0]
        # been given ids.
        else:
            arg_source = kwargs["node1"] if "node1" in kwargs else args[0]
            arg_target = kwargs["node2"] if "node2" in kwargs else args[1]

    def has_node(self, node):
        """Checks if a node exists in the graph."""
        return self.node(node) is not None

    def has_edge(self, edge):
        """Checks if an edge exists in the graph."""
        return edge in self._has_edge_cache


graph = Graph()
