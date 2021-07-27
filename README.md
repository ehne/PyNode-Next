  
<p>
  <img alt="logo" src="./assets/card.png" align="center" />
</p>

# PyNode-Next
A complete rewrite of PyNode for the modern era.

Goals: 
- implement all features of PyNode https://alexsocha.github.io/pynode/

Graph
- [x] graph.add_node(node) - Adds a node to the graph.
- [x] graph.add_node(id=None, value=id) - Creates a Node(id, value) and adds it to the graph.
- [ ] graph.remove_node(node) - Removes a node from the graph.
- [x] graph.node(id) - Returns a node in the graph by its id.
- [ ] graph.nodes() - Returns a list of all nodes in the graph.
 
- [ ] graph.add_edge(edge) - Adds an edge to the graph.
- [ ] graph.add_edge(source, target, weight=None, directed=False) - Creates an Edge(source, target, weight, directed) and adds it to the graph.
- [ ] graph.remove_edge(edge) - Removes an edge from the graph.
- [ ] graph.remove_edge(node1, node2, directed=False) - Removes edge(s) between node1 and node2. If directed is set, only edges beginning at node1 will be removed.
 
- [ ] graph.has_node(node) - Checks whether a node has been added to the graph.
- [ ] graph.has_edge(edge) - Checks whether an edge has been added to the graph.
- [ ] graph.adjacent(node1, node2, directed=False) - Checks whether an edge exists between node1 and node2. If directed is set, the edge must begin at node1.
- [ ] graph.edges_between(node1, node2, directed=False) - Returns a list of all edges between node1 and node2. If directed is set, only edges beginning at node1 will be included.
 
- [ ] graph.set_directed(directed=True) - Sets whether all edges in the graph are directed.
- [ ] graph.adjacency_matrix() - Creates and returns an adjacency matrix (2-dimensional dictionary, using node id values as keys) for the graph.
- [ ] graph.add_all(elements) - Adds a list of Node and/or Edge elements to the graph.
- [ ] graph.remove_all(elements) - Removes a list of Node and/or Edge elements from the graph.
- [ ] graph.random(order, size, connected=True, multigraph=False, initial_id=0) - Returns a list of randomly connected nodes and edges, with order specifying the amount of nodes and size specifying the amount of edges. If connected is set, a path will exist between any pair of nodes (unless the amount of edges makes this impossible). If multigraph is set, a pair of nodes may be connected by multiple edges. Nodes are assigned incremental id values starting at initial_id.
- [ ] graph.order(), graph.size() - Returns the number of nodes/edges in the graph.
- [ ] graph.clear() - Deletes all nodes and edges from the graph.
Note: All functions containing node parameters accept either a Node instance or node id value.
 
Node
- [x] Node(id=None, value=id) - Creates a node with the specified id and value. Assigns a unique id integer if the specified id is None.
- [ ] node.id() - Returns the id of the node.
- [ ] node.set_value(), node.value() - Sets/gets the value of the node.
- [ ] node.incident_edges(), node.incoming_edges(), node.outgoing_edges() - Returns a list of the node's incident/incoming/outgoing edges.
- [ ] node.adjacent_nodes(), node.predecessor_nodes(), node.successor_nodes() - Returns a list of the node's adjacent/predecessor/successor nodes.
- [ ] node.degree(), node.indegree(), node.outdegree() - Returns the node's degree/indegree/ outdegree.
- [ ] node.set_attribute(name, value), node.attribute(name) - Sets/gets custom attributes for the node.
- [ ] node.set_priority(value), node.priority(name) - Sets/gets a priority value used for comparison.
 
- [ ] node.set_position(x, y, relative=False) - Sets the static position of the node. x and y are pixel coordinates, with (0, 0) being the top-left corner of the output window (the standard size of the window is 500x400). If relative is set, x and y should instead be values between 0.0 and 1.0, specifying the node's position as a percentage of the window size.
- [ ] node.position() - Returns a tuple with the (x, y) coordinates of the node. Should be used in asynchronous function calls.
- [ ] node.set_label(value, label_id=0), node.label(label_id) - Sets/gets the value of additional labels for the node (Use label_id=0 for the top-right label and label_id=1 for the top left-label).
- [ ] node.set_size(size=12), node.size() - Sets/gets the radius of the node.
- [ ] node.set_color(color=Color.DARK_GREY), node.color() - Sets/gets the color of the node.
- [ ] node.set_value_style(size=13, color=Color.WHITE, outline=None) - Sets the appearance of the node's value text (if no outline is specified, the node's background color will be used for the outline).
- [ ] node.set_label_style(size=10, color=Color.GREY, outline=None, lable_id=None) - Sets the appearance of the node's label text (if no lable_id is specified, both labels will be affected).
- [ ] node.highlight(color=node.color(), size=node.size()*1.5) - Performs a highlight animation by temporarily changing the size and color of the node.
 
Edge
- [ ] Edge(source, target, weight=None, directed=False) - Creates an edge between the specified source and target nodes, with optional weight and directed properties.
- [ ] edge.source(), edge.target() - Returns the edge's source/target nodes.
- [ ] edge.set_weight(weight=None), edge.weight() - Sets/gets the weight of the edge.
- [ ] edge.set_directed(directed=True), edge.directed() - Sets/gets whether the edge is directed.
- [ ] edge.other_node(node) - Returns a node connected by the edge, other than the node specified.
- [ ] edge.set_attribute(name, value), edge.attribute(name) - Sets/gets custom attributes for the edge.
- [ ] edge.set_priority(value), edge.priority(name) - Sets/gets a priority value used for c-omparison.
 
- [ ] edge.set_width(width=2), edge.width() - Sets/gets the width of the edge.
- [ ] edge.set_color(color=Color.LIGHT_GREY), edge.color() - Sets/gets the color of the edge.
- [ ] edge.set_weight_style(size=10, color=Color.GREY, outline=None) - Sets the appearance of the edge's weight text.
- [ ] edge.highlight(color=edge.color(), width=edge.width()*2) - Performs a highlight animation by temporarily changing the width and color of the edge.
- [ ] edge.traverse(initial_node=edge.source(), color=Color.RED, keep_path=True) - Performs a traversal animation on the edge, beginning at initial_node and using the specified color. If keep_path is set, the edge will remain colored.
 
Miscellaneous
- [x] Color(red, green, blue) - Custom color for use in node and edge animations, using 0-255 values for each component.
- [x] Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.WHITE, Color.LIGHT_GREY, Color.GREY, Color.DARK_GREY, Color.BLACK, Color.TRANSPARENT - Predefined colors for use in node and edge animations.
- [x] pause(time) - Delays the next visual event for the specified number of milliseconds (note that this does not pause code execution).
- [ ] delay(func, time, args=[], repeat=False) - Executes a function after the specified number of milliseconds, with the optional args list of parameters. If repeat is set, the function will execute continuously until the delay is cancelled. Returns a delay_id integer referencing the delay.
- [ ] cancel_delay(delay_id) - Cancels a scheduled delay event.
- [ ] register_click_listener(func) - Registers a function which will be called whenever a node is clicked. The function must include a node parameter (e.g. def on_click(node)), which will receive the instance of the clicked node.