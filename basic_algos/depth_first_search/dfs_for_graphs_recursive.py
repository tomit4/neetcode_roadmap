from typing import Dict, List


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # List to store neighboring nodes


# Create nodes
node_a = GraphNode("A")
node_b = GraphNode("B")
node_c = GraphNode("C")
node_d = GraphNode("D")
node_e = GraphNode("E")

# Connect nodes
node_a.neighbors = [node_b, node_c]
node_b.neighbors = [node_a]
node_c.neighbors = [node_a, node_d, node_e]
node_d.neighbors = [node_c]
node_e.neighbors = [node_c]


def dfs_graph(node: GraphNode):
    visited = set()

    def dfs(current_node: GraphNode):
        if current_node in visited:
            return
        visited.add(current_node)  # Mark as visited
        print(current_node.value)  # Process the node
        for neighbor in current_node.neighbors:
            dfs(neighbor)  # Recur for each neighbor

    dfs(node)


# Adjacency List
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}

######  0
#####  / \
####  1   2
###  / \    \
##  3   4    5


def is_connected(graph: Dict[int, List[int]]) -> bool:
    visited = set()

    def dfs(node):
        if node in visited:  # Base case: node already visited
            return
        visited.add(node)  # Mark the current node as visited
        for neighbor in graph[node]:  # Recur for all neighbors
            dfs(neighbor)

    # Start DFS from any node (e.g. node 0)
    start_node = next(iter(graph))  # Get an arbitrary node
    dfs(start_node)

    return len(visited) == len(graph)


def generic_dfs(graph: Dict[int, List[int]]):
    visited = set()  # Track visited nodes

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        # Process the node (e.g., print or collect data)
        print(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    # Iterate over all nodes to ensure we cover disconnected components
    for node in graph:
        if node not in visited:
            dfs(node)
