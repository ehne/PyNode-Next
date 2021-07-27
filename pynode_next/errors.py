from .core import core

class Error(Exception):
    """The base error exception."""
    def __init__(self, message):
        print("send error to ax")
        # self.canvas.dispatch(dispatch_dict)
        core.ax(lambda x: x.dispatch({"isPyNodeNext": True, "type": "error", "message": message}))

class DuplicateNodeError(Error):
    """Raised when a node with the same id as a previous one was added."""
    pass