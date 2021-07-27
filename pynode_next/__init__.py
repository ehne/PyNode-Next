import algorithmx as algx
from pathlib import Path
import os


from .color import *


class Node:
    pass

class Edge:
    pass

class Core:
    def __init__(self, port=5050):
        base_path = os.path.relpath(__file__)
        custom_ui = f"{Path(base_path).parent}/ui.html"

        print("serving ui found at", custom_ui)
        self.server = algx.http_server(port=port, file=custom_ui)

        self.canvas = self.server.canvas()

    def run(self, func):
        """A decorator that runs a function in the PyNode Next web environment."""
        def wrapper():
            self.canvas.onmessage("start", func)
            print(
                f"staring server on http://localhost:{self.port} — press ctrl+c to quit"
            )
            self.server.start()

        return wrapper
    
    def _ax(self):
        """A function that does all of the interfacing with AlgorithmX"""
        pass
    

