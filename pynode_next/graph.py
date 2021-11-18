from typing import Union, Iterable
from random import randint, choices
from .overloading import overloaded, overloads

from .misc import Color, pause
from .node import Node
from .errors import NodeDoesntExistError, DuplicateEdgeError, DuplicateNodeError
from .edge import Edge
from .core import core

_generic_text = Union[str, int, float]

class Graph:
    def __init__(self):
        self._nodes = {}
        self._edges = []
        self._has_edge_cache = {}

    def add(self, element):
        """Adds either a node or an edge object to the graph"""
        elem_type = type(element)
        if elem_type == Node:
            # Make sure there aren't two nodes with the same id
            if element._id in self._nodes:
                raise DuplicateNodeError(f"Duplicate node with id '{element._id}'")

            # add node to dict and canvas
            self._nodes[element._id] = element
            element._in_graph = True
            # just sends all of the node's data
            core.ax(lambda x: x.dispatch(element._data()))
            # sets the node's click handler
            if core.callback != None:
                core.ax(lambda x: x.nodes([element._id]).onclick(core.callback))
            return element
        elif elem_type == Edge:
            e = element
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
            if e._source is None:
                raise NodeDoesntExistError(
                    f"The node {original_source} does not exist in the graph"
                )
            if e._target is None:
                raise NodeDoesntExistError(
                    f"The node {original_target} does not exist in the graph"
                )

            # adds the incident edges to the nodes
            e._source._incident_edges.append(e)
            e._target._incident_edges.append(e)

            self._edges.append(e)
            self._has_edge_cache[e] = True

            e._in_graph = True
            core.ax(lambda x: x.dispatch(e._data()))
            return e

    def remove(self, element):
        """Removes the specified element (either a Node or an Edge object) from the graph."""
        elem_type = type(element)
        if elem_type == Node:
            for edge in element._incident_edges:
                self.remove(edge)

            del self._nodes[element._id]
            core.ax(lambda x: x.node(str(element._id)).remove())

            return element
        elif elem_type == Edge:
            element._source._incident_edges.remove(element)
            element._target._incident_edges.remove(element)

            self._edges.remove(element)
            del self._has_edge_cache[element]

            core.ax(
                lambda x: x.dispatch(
                    {"attrs": {"edges": {str(element._internal_id): {"remove": True}}}}
                )
            )

            return element

    def add_node(self, id, value=None):
        """Adds a node to the graph using an id."""
        if value is None:
            value = id
        return self.add(Node(id, value))

    def remove_node(self, node):
        """Removes the specified node id from the graph"""
        return self.remove(self.node(node))

    def node(self, node):
        """Returns the node specified"""
        node_id = ""
        if isinstance(node, Node):
            node_id = node._id
        else:
            node_id = node
        
        if node_id in self._nodes:
            return self._nodes[node_id]
        raise NodeDoesntExistError(f"The node '{node_id}' <{type(node).__name__}> does not exist in the graph")

    def nodes(self):
        """Returns all of the graph's nodes."""
        return list(self._nodes.values())

    def add_edge(self, source, target, weight="", directed: bool = False):
        """Adds an edge by defining it's relation to other nodes."""
        return self.add(Edge(source, target, weight, directed))

    def remove_edge(self, nodeA, nodeB, directed: bool = False):
        """Removes the specified edge(s) between two nodes from the graph"""
        edges_between = self.edges_between(nodeA, nodeB, directed)
        edge_list = []
        for edge in edges_between:
            edge_list.append(edge_list)
            self.remove(edge)
        return edge_list

    def has_node(self, node):
        """Checks if a node exists in the graph."""
        return self.node(node) is not None

    def add_all(self, elements: Iterable[Union[Node, Edge]]):
        """Adds all node and edge objects from an iterable. all elements need to be of the type `Node` or `Edge`"""
        for i in elements:
            self.add(i)
            pause(20)

    def remove_all(self, elements: Iterable[Union[Node, Edge]]):
        """Removes all node and edge objects from an iterable. all elements need to be of the type `Node` or `Edge`"""
        for i in elements:
            if isinstance(i, Node):
                self.remove_node(i)
            elif isinstance(i, Edge):
                self.remove_edge(i)
            pause(20)

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

    def adjacent(self, nodeA, nodeB, directed=False):
        """Checks if an edge between nodeA and nodeB exists. If directed is True, then the edge must start from nodeA"""
        nodeA = self.node(nodeA)
        nodeB = self.node(nodeB)

        node_list = nodeA.adjacent_nodes()
        if directed:
            node_list = nodeA.successor_nodes()

        for n in node_list:
            if n is nodeB:
                return True
        return False

    def clear(self):
        """Completely resets the entire graph."""
        es = list(self._edges)
        for e in es:
            self.remove_edge(e)
        ns = list(self._nodes)
        for n in ns:
            self.remove_node(n)
        return self

    def set_directed(self, directed=True):
        """Sets whether or not all of the edges in the graph are directed."""
        for i in self._edges:
            i.set_directed(directed)
        return self

    def order(self):
        """Returns the order of the graph. that is, the number of nodes"""
        return len(self._nodes)

    def size(self):
        """Returns the size of the graph. that is, the number of edges"""
        return len(self._edges)

    def adjacency_matrix(self):
        """Returns the adjacency matrix of the graph as a dictionary"""
        matrix = {}
        # goes through and creates an empty row for each node
        for r in self.nodes():
            current_row = {}
            for c in self.nodes():
                # sets default connectedness
                current_row[c._id] = 0
            matrix[r._id] = current_row

        # sets the values correctly
        for r in self.nodes():
            for c in r.successor_nodes():
                matrix[r._id][c._id] += 1

        return matrix

    def _register_click_handler(self, func):
        new_func = lambda n: func(self.node(n))
        core.callback = new_func
        node_list = [i._id for i in self.nodes()]
        core.ax(lambda x: x.nodes(node_list).onclick(new_func))

    @staticmethod
    def random(order, size):
        """Returns a random list of edges and nodes that may or may not be connected."""
        nodes = []
        edges = []

        for i in range(order):
            nodes.append(Node(str(i)))

        while len(edges) != size:
            source_node, target_node = choices(population=nodes, k=2)
            e = Edge(source_node, target_node)
            edges.append(e)

        return nodes + edges


graph = Graph()
register_click_handler = graph._register_click_handler