import uuid

from .misc import *


class Edge:
    def __init__(self, source, target, weight=None, directed=False):
        self._source = source
        self._target = target
        self._weight = weight
        self._directed = directed

        self._color = Color.LIGHT_GREY

        self._internal_id = uuid.uuid4()

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

    def traverse(self, initial_node=None, color=Color.RED, keep_path=True):
        if initial_node == None:
            source = self._source
        else:
            source = initial_node

        core.ax(
            lambda x: x.dispatch(
                {
                    "attrs": {
                        "edges": {
                            str(self._internal_id): {
                                "color": {
                                    "animtype": "traverse",
                                    "value": str(color),
                                    "animsource": source._id,
                                }
                            }
                        }
                    }
                }
            )
        )
        # undoes the traversal color
        if not keep_path:
            pause(500)
            core.ax(
                lambda x: x.dispatch(
                    {
                        "attrs": {
                            "edges": {
                                str(self._internal_id): {
                                    "color": {"value": str(self._color)}
                                }
                            }
                        }
                    }
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
                    }
                }
            }
        }
