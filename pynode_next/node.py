from .misc import Color
from .core import core

class Node:
    def __init__(self, id, value):
        self._id = id
        self._value = value

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

    def set_color(self, color=Color.DARK_GREY):
        """Sets the node's color to the Color object specified."""
        self._color = color
        core.ax(lambda x: x.node(self._id).color(str(self._color)))
        return self

    def color(self):
        return self._color

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

    def _data(self):
        """used internally to generate data to dispatch to algx"""
        return {
            "attrs": {
                "nodes": {
                    self._id: {
                        "color": str(self._color),
                        "labels": {
                            0: {
                                "text": self._value
                            }
                        }
                    }
                }
            }
        }

if __name__ == "__main__":
    assert Node(id="cool")._value == "cool"
    assert Node("cool")._value == "cool"
    assert Node(id="cool", value="hi")._value == "hi"
    assert Node("cool", "hi")._value == "hi"
