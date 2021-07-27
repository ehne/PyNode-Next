import algorithmx as algx
from pathlib import Path
import os


class Core:
    def __init__(self, port=5050):
        self.port = 5050
        base_path = os.path.relpath(__file__)
        custom_ui = f"{Path(base_path).parent}/ui.html"

        print("serving ui found at", custom_ui)
        self.server = algx.http_server(port=port, file=custom_ui)

        self.canvas = self.server.canvas()

    def run(self, func):
        """A function that runs a different function in the PyNode Next web environment."""
        self.canvas.onmessage("start", func)
        print(f"staring server on http://localhost:{self.port} — press ctrl+c to quit")
        self.server.start()

    def ax(self, func):
        """lets functions outside of this class interface with AlgorithmX."""
        func(self.canvas)


core = Core()