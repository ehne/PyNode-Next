import sys
from .core import core

class Error(RuntimeError):
    """The base error exception."""
    def __init__(self, message):
        # self.canvas.dispatch(dispatch_dict)
        super().__init__(message)
        self.message = message
        # core.ax(lambda x: x.dispatch({"isPyNodeNext": True, "type": "error", "message": self.message}))

class DuplicateNodeError(Error):
    """Raised when a node with the same id as a previous one was added."""

class DuplicateEdgeError(Error):
    """Raised when a edge with the exact same values has been added to the graph."""

class NodeDoesntExistError(Error):
    """Raised when a node does not exist in the graph"""

class NodePositionError(Error):
    """Raised when a node's position is set with the relative argument set to false"""