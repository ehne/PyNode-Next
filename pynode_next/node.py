from .misc import Color
from .core import core

class Node:
    def __init__(self, *args, **kwargs):
        arg_id = kwargs["id"] if "id" in kwargs else args[0]
        self._id = arg_id

        arg_value = kwargs["value"] if "value" in kwargs else args[1] if len(args) > 1 else arg_id
        self._value = arg_value

        self._incident_edges = []
        self._color = Color.DARK_GREY
    
    def id(self):
        """Returns the node's id"""
        return self._id

    def set_value(self, value):
        """Sets the node's value."""
        self._value = value
        core.ax(lambda x: x.node(self._id).label().text(value))

    def value(self):
        """Returns the node's value."""
        return self._value

    def incident_edges(self):
        """Returns the incident edges through the node."""
        return list(self._incident_edges)
    
    def incoming_edges(self):
        """Returns the edges going into the node"""
        return [e for e in self._incident_edges if not e._directed or e._target == self]

    def outgoing_edges(self):
        """Returns the edges going out of the node"""
        return [e for e in self._incident_edges if not e._directed or e._source == self]

    def degree(self):
        """Returns the degree of the node."""
        return len(self._incident_edges)
    
    def indegree(self): 
        """Returns the number of edges going into the node."""
        return len(self.incoming_edges())
        
    def outdegree(self): 
        """Returns the number of edges going out of the node."""
        return len(self.outgoing_edges())

    def __str__(self):
        return str(self._id)

if __name__ == "__main__":
    assert Node(id="cool")._value == "cool"
    assert Node("cool")._value == "cool"
    assert Node(id="cool", value="hi")._value == "hi"
    assert Node("cool", "hi")._value == "hi"
