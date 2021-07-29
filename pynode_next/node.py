import uuid

from .misc import Color
from .core import core


class Node:
    def __init__(self, id=None, value=None):
        if id != None:
            self._id = id
        else:
            self._id = str(uuid.uuid4())

        if value != None:
            self._value = value
        else:
            self._value = self._id

        self._incident_edges = []
        self._color = Color.DARK_GREY

        self._attrs = {}

        self._labels = {}

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

    def set_attribute(self, name, value):
        """Sets an attribute of a node"""
        self._attrs[name] = value

    def attribute(self, name):
        """Returns a nodes named attribute"""
        return self._attrs[name]

    def set_label(self, value, label_id=0):
        """Sets a node's label. 0 for top right and 1 for top left."""
        self._labels[0] = value
        label = ["tr", "tl"][label_id]
        label_angle = [45, 45 + 90][label_id]

        core.ax(
            lambda x: x.dispatch(
                {
                    "attrs": {
                        "nodes": {
                            self._id: {
                                "labels": {label: {"angle": label_angle, "text": value}}
                            }
                        }
                    }
                }
            )
        )

    def label(self, label_id=0):
        return self._labels[label_id]

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

    def adjacent_nodes(self):
        """Returns a list of nodes that are adjacent to this node."""
        node_list = []
        for e in self._incident_edges:
            if e._target is self:
                node_list.append(e._source)
            else:
                node_list.append(e._target)
        return node_list

    def predecessor_nodes(self):
        node_list = []
        for e in self.incoming_edges():
            if e._target is self:
                node_list.append(e._source)
            else:
                node_list.append(e._target)
        return node_list

    def successor_nodes(self):
        node_list = []
        for e in self.outgoing_edges():
            if e._target is self:
                node_list.append(e._source)
            else:
                node_list.append(e._target)
        return node_list

    def __str__(self):
        return str(self._id)

    def _data(self):
        """used internally to generate data to dispatch to algx"""
        return {
            "attrs": {
                "nodes": {
                    self._id: {
                        "color": str(self._color),
                        "labels": {0: {"text": self._value}},
                    }
                }
            }
        }


if __name__ == "__main__":
    assert Node(id="cool")._value == "cool"
    assert Node("cool")._value == "cool"
    assert Node(id="cool", value="hi")._value == "hi"
    assert Node("cool", "hi")._value == "hi"
