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
            raise DuplicateNodeError(f"Duplicate node with id '{n._id}'")

        # add node to dict and canvas
        self._nodes[n._id] = n
        # just sends all of the node's data
        core.ax(lambda x: x.dispatch(n._data()))
        return n

    def remove_node(self, node):
        pass

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
    
    def add_edge(self, *args, **kwargs):
        """Add an edge to the graph."""
        # checks if edge is defined like add_edge(edge=Edge())
        if "edge" in kwargs:
            e = kwargs["edge"]
        # checks if the edge is defined like add_edge(Edge())
        elif len(args) > 0 and isinstance(args[0], Edge):
            e = args[0]
        else:
            # splits up the args in their actual variables
            arg_source = kwargs["source"] if "source" in kwargs else args[0]
            arg_target = kwargs["target"] if "target" in kwargs else args[1]
            arg_weight = kwargs["weight"] if "weight" in kwargs else args[2] if len(args) > 2 else None
            arg_directed = kwargs["directed"] if "directed" in kwargs else args[3] if len(args) > 3 else False
            # makes a new edge
            e = Edge(arg_source, arg_target, arg_weight, arg_directed)
        if self.has_edge(e):
            raise DuplicateEdgeError(f"There is already an instance of the edge '{e}' in the graph")
        
        # saves the original sources so we can check if they actually exist in the graph
        original_source = e._source
        original_target = e._target

        e._source = self.node(e._source)
        e._target = self.node(e._target)
        
        if e._source == None:
            raise NodeDoesntExistError(f"The node {original_source} does not exist in the graph")
        if e._target == None:
            raise NodeDoesntExistError(f"The node {original_target} does not exist in the graph")

        # adds the incident edges to the nodes
        e._source._incident_edges.append(e)
        e._target._incident_edges.append(e)

        self._edges.append(e)
        self._has_edge_cache[e] = True
        
        # TODO: below should just dispatch the edge's data so that add_edge(Edge()) is fully supported
        core.ax(lambda x: x.edge((e._source._id, e._target._id)).add(color=str(e._color), directed=e._directed))
        return e

    def has_node(self, node):
        """Checks if a node exists in the graph."""
        return self.node(node) is not None

    def has_edge(self, edge):
        """Checks if an edge exists in the graph."""
        return edge in self._has_edge_cache

graph = Graph()