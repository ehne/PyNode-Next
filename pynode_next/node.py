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

if __name__ == "__main__":
    assert Node(id="cool")._value == "cool"
    assert Node("cool")._value == "cool"
    assert Node(id="cool", value="hi")._value == "hi"
    assert Node("cool", "hi")._value == "hi"
