import uuid

from .misc import *


class Edge:
    def __init__(self, source, target, weight=None, directed=False):
        self._source = source
        self._target = target
        self._directed = directed

        self._weight = weight
        if weight == None:
            self._weight = ""

        self._color = Color.LIGHT_GREY

        self._internal_id = uuid.uuid4()

        self._attrs = {}

    def _dispatch_wrapper(self, x, in_dict):
        """Returns the in_dict inside of the attrs.edges[self._internal_id] dictionary, so it's slightly less bulky to look at."""
        return x.dispatch({"attrs": {"edges": {str(self._internal_id): in_dict}}})

    def other_node(self, node):
        """Returns the other node than the specified node in the edge."""
        return (
            self._target
            if (self._source is node or self._source._id == node)
            else self._source
        )

    def source(self, target=None):
        """Returns the edge's source node."""
        if target != None:
            return self.other_node(target)
        return self._source

    def target(self, source=None):
        """Returns the edge's target node."""
        if source != None:
            return self.other_node(source)
        return self._target

    def set_attribute(self, name, value):
        """Sets an attribute of the edge"""
        self._attrs[name] = value

    def attribute(self, name):
        """Gets an attribute of the edge"""
        return self._attrs[name]

    def set_color(self, color):
        """Sets the colour of the edge. `color` needs to be a Color() object"""
        self._color = color
        core.ax(
            lambda x: self._dispatch_wrapper(
                x,
                {
                    "color": {
                        "value": str(color),
                    }
                },
            )
        )
        return self

    def color(self):
        """Gets the edge's color."""
        return self._color

    def set_weight(self, weight):
        """Sets the edge's weight. (Weight must be serialisable)"""
        self._weight = weight
        core.ax(
            lambda x: self._dispatch_wrapper(x, {"labels": {1: {"text": str(weight)}}})
        )
        return self

    def weight(self):
        """Returns the edge's weight. Returns an empty string if weight wasn't defined at init and hasn't been changed since."""
        return self._weight

    def set_directed(self, directed=True):
        """Sets whether or not the edge is directed"""
        self._directed = directed
        core.ax(lambda x: self._dispatch_wrapper(x, {"directed": directed}))
        return self
    
    def directed(self):
        """Returns whether or not the edge is directed"""
        return self._directed
        
    def traverse(self, initial_node=None, color=Color.RED, keep_path=True):
        if initial_node == None:
            source = self._source
        else:
            source = initial_node

        core.ax(
            lambda x: self._dispatch_wrapper(
                x,
                {
                    "color": {
                        "animtype": "traverse",
                        "value": str(color),
                        "animsource": source._id,
                    }
                },
            )
        )

        # undoes the traversal color
        if not keep_path:
            pause(500)
            core.ax(
                lambda x: self._dispatch_wrapper(
                    x, {"color": {"value": str(self._color)}}
                )
            )
        else:
            # stores the changed color
            self._color = color

    def __str__(self):
        return f"({self._source}, {self._target})"

    def _data(self):
        """used internally to generate data to dispatch to algx"""
        return {
            "attrs": {
                "edges": {
                    f"{self._internal_id}": {
                        "color": str(self._color),
                        "source": str(self._source),
                        "target": str(self._target),
                        "directed": self._directed,
                        "labels": {1: {"text": str(self._weight)}},
                    }
                }
            }
        }
