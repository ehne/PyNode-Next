from .core import core

class Error(Exception):
    """The base error exception."""
    def __init__(self, message):
        # self.canvas.dispatch(dispatch_dict)
        core.ax(lambda x: x.dispatch({"isPyNodeNext": True, "type": "error", "message": message}))

class DuplicateNodeError(Error):
    """Raised when a node with the same id as a previous one was added."""
    pass

class DuplicateEdgeError(Error):
    """Raised when a edge with the exact same values has been added to the graph."""
    pass

class NodeDoesntExistError(Error):
    """Raised when a node does not exist in the graph"""
    pass