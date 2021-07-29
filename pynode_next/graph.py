from typing import Union, Iterable
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
        return self.add_node(id, id)

    @overloads(add_node)
    def add_node(self, id: str, value: str):
        """Adds a node to the graph using an id and a value."""
        if value == None:
            value = id
        return self.add_node(Node(id, value))

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
        """Removes the specified node from the graph"""
        n = self.node(node)

        for edge in n._incident_edges:
            self.remove_edge(edge)

        del self._nodes[n._id]
        core.ax(lambda x: x.node(str(n._id)).remove())
        return n

    @overloaded
    def node(self, id: str):
        """Returns the node with the id specified."""
        if id in self._nodes:
            return self._nodes[id]
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
    def add_edge(self, source, target, weight=None, directed: bool = False):
        """Adds an edge by defining it's relation to other nodes."""
        return self.add_edge(Edge(source, target, weight, directed))

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

        core.ax(lambda x: x.dispatch(e._data()))
        return e

    @overloaded
    def remove_edge(self, nodeA, nodeB, directed: bool = False):
        edges_between = self.edges_between(nodeA, nodeB, directed)
        edge_list = []
        for edge in edges_between:
            edge_list.append(edge_list)
            self.remove_edge(edge)
        return edge_list

    @overloads(remove_edge)
    def remove_edge(self, edge: Edge):
        """Removes an edge object from the graph"""
        edge._source._incident_edges.remove(edge)
        edge._target._incident_edges.remove(edge)

        self._edges.remove(edge)
        del self._has_edge_cache[edge]

        core.ax(
            lambda x: x.dispatch(
                {"attrs": {"edges": {str(edge._internal_id): {"remove": True}}}}
            )
        )

        return edge

    def has_node(self, node):
        """Checks if a node exists in the graph."""
        return self.node(node) is not None

    def add_all(self, elements: Iterable[Union[Node, Edge]]):
        """Adds all node and edge objects from an iterable"""
        for i in elements:
            if isinstance(i, Node):
                self.add_node(i)
            elif isinstance(i, Edge):
                self.add_edge(i)

    def has_edge(self, edge):
        """Checks if an edge exists in the graph."""
        return edge in self._has_edge_cache

    def edges_between(self, nodeA, nodeB, directed=False):
        """Returns all edges between the two nodes nodeA and nodeB. Setting directed to True means that the edges it returns will only be from nodeA to nodeB"""
        if not self.has_node(nodeA) or not self.has_node(nodeB):
            return []

        if directed:
            edge_list = self.node(nodeA).outgoing_edges()
        else:
            edge_list = self.node(nodeA).incident_edges()

        out_edges = []
        for edge in edge_list:
            if edge._target is self.node(nodeB) or edge._source is self.node(nodeB):
                out_edges.append(edge)

        return out_edges


graph = Graph()
