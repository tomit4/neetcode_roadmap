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


def dfs_iterative(start_node):
    visited = set()  # Track visited nodes
    stack = [start_node]  # Initialize stack with the starting node

    while stack:
        current_node = stack.pop()  # Pop the last node from the stack

        if current_node in visited:
            continue  # skip already visited nodes

        visited.add(current_node)  # Mark node as visited
        print(current_node.value)  # Process the node

        # Add neighbors to the stack (order matters for traversal)
        for neighbor in reversed(current_node.neighbors):
            if neighbor not in visited:
                stack.append(neighbor)
