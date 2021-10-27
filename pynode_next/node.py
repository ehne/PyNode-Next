from pynode_next.errors import NodePositionError
import uuid

from .misc import Color
from .core import core


class Node:
    def __init__(self, id=None, value=None):
        if id is not None:
            self._id = id
        else:
            self._id = str(uuid.uuid4())

        if value is not None:
            self._value = value
        else:
            self._value = self._id

        self._incident_edges = []
        self._color = Color.DARK_GREY
        self._size = 12
        self._priority = 0
        self._attrs = {}
        self._labels = {}
        self._pos = []

        self._in_graph = False

    # __ makes a private method
    def __ax(self, func):
        """Runs the specified AlgorithmX function only if the node is in the graph"""
        if self._in_graph:
            core.ax(func)

    def id(self):
        """Returns the node's id"""
        return self._id

    def set_value(self, value):
        """Sets the node's value."""
        self._value = value
        self.__ax(lambda x: x.node(self._id).label().text(value))
        return self

    def value(self):
        """Returns the node's value."""
        return self._value

    def set_value_style(self, size=13, color=Color.WHITE, outline=None):
        if outline is not None:
            print("set_value_style(outline) is not supported by PyNode_Next")
        self.__ax(lambda x: x.node(self._id).label().size(size).color(str(color)))
        return self

    def set_size(self, size=12):
        """Sets the size of a node"""
        self._size = size
        self.__ax(lambda x: x.node(self._id).size(size))
        return self

    def size(self):
        """Returns the node's size"""
        return self._size

    def set_priority(self, value):
        """Sets a node's priority value."""
        self._priority = value
        return self

    def priority(self):
        """Gets a node's priority"""
        return self._priority

    def set_color(self, color=Color.DARK_GREY):
        """Sets the node's color to the Color object specified."""
        self._color = color
        self.__ax(lambda x: x.node(self._id).color(str(self._color)))
        return self

    def color(self):
        return self._color

    def highlight(self, color=None, size=None):
        """Highlights a node for a small time, by increasing its size and changing its color."""
        old_size = self._size

        new_size = size
        if size is None:
            new_size = old_size * 1.5

        old_color = self._color

        new_color = color
        if color is None:
            new_color = Color.RED

        self.__ax(
            lambda x: x.node(self._id)
            .color(str(new_color))
            .size(new_size)
            .pause(0.5)
            .color(str(old_color))
            .size(old_size)
        )

        return self

    def set_attribute(self, name, value):
        """Sets an attribute of a node"""
        self._attrs[name] = value
        return self

    def attribute(self, name):
        """Returns a nodes named attribute"""
        return self._attrs[name]

    def set_label(self, value, label_id=0):
        """Sets a node's label. 0 for top right and 1 for top left."""
        self._labels[0] = value
        label = ["tr", "tl"][label_id]
        label_angle = [45, 45 + 90][label_id]

        self.__ax(lambda x: x.node(self._id).label(label).angle(label_angle).text(value))
        return self

    def label(self, label_id=0):
        return self._labels[label_id]

    def set_label_style(self, size=10, color=Color.GREY, outline=None, label_id=None):
        """Sets the style of any labels"""
        if outline is not None:
            print("set_label_style(outline) is not supported by PyNode Next")
        if label_id is None:
            self.__ax(lambda x: x.node(self._id).label('tr').size(size).color(str(color)))
            self.__ax(lambda x: x.node(self._id).label('tl').size(size).color(str(color)))
        else:
            label = ["tr", "tl"][label_id]
            self.__ax(lambda x: x.node(self._id).label(label).size(size).color(str(color)))
        return self

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

    def set_position(self, x, y, relative=True):
        """Sets the node's position. Relative is the only style you can use"""
        if not relative:
            raise NodePositionError("Cannot call node.set_position() with relative=False")
        
        self._pos = [x, y]
        
        x_norm = core.normalise_to_canvas(x)
        y_norm = core.normalise_to_canvas(y)
        self.__ax(lambda a: a.node(self._id).pos((f"{x_norm}cx", f"{y_norm}cy")))
        return self

    def position(self):
        """Returns the node's relative position as a list of [x, y]"""
        return self._pos
    
    def __str__(self):
        return str(self._id)

    def _data(self):
        """used internally to generate data to dispatch to algx."""
        base = {
            "attrs": {
                "nodes": {
                    self._id: {
                        "color": str(self._color),
                        "labels": {0: {"text": self._value}},
                        "listenclick": True,
                        "size": self._size
                    }
                }
            }
        }

        if 0 in self._labels.keys():
            base['attrs']['nodes'][self._id]['labels']['tr'] = { 'angle': 45, 'text': self._labels[0] }
        if 1 in self._labels.keys():
            base['attrs']['nodes'][self._id]['labels']['tl'] = { 'angle': 135, 'text': self._labels[1] }

        if self._pos != []:
            base["attrs"]["nodes"][self._id]["pos"] = [core.normalise_to_canvas(i) for i in self._pos]

        return base


if __name__ == "__main__":
    assert Node(id="cool")._value == "cool"
    assert Node("cool")._value == "cool"
    assert Node(id="cool", value="hi")._value == "hi"
    assert Node("cool", "hi")._value == "hi"
