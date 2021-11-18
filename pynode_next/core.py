import algorithmx as algx
from pathlib import Path
from .pynode_version import version
import os


class Core:
    def __init__(self, port=5050):
        self.port = port
        base_path = os.path.relpath(__file__)
        self.custom_ui = f"{Path(base_path).parent}/ui.html"
        self.callback = lambda: None
      

    def run(self, func, check_for_new_version):
        """A function that runs a different function in the PyNode Next web environment."""
        while 1:
            try:
                self.server = algx.http_server(port=self.port, file=self.custom_ui)
                break
            except OSError:
                self.port += 1
        print("serving ui found at", self.custom_ui)
        
        self.canvas = self.server.canvas()
        def pynode_func():
            # self.canvas.duration(0).zoom(1.7)
            func()
        self.canvas.onmessage("start", pynode_func)

        if check_for_new_version:
            version_dispatch_dict = {'isPyNodeNext': True, 'type': 'version', 'message': version}
            self.canvas.onmessage("getVersion", lambda: self.canvas.dispatch(version_dispatch_dict))

        print(f"staring server on http://localhost:{self.port} — press ctrl+c to quit")
        self.server.start()

    def ax(self, func):
        """lets functions outside of this class interface with AlgorithmX."""
        func(self.canvas)

    def jupyter(self, width=200, height=200):
        self.canvas = algx.jupyter_canvas()
        self.canvas.size((width, height))
        # print("loaded Canvas")
        display(self.canvas)

    def normalise_to_canvas(self, val):
        """Normalises a relative position that is an element of the interval [0, 1] to the interval [-1, 1]"""
        # formula used: (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 
        return (val * 2) - 1
        

core = Core()