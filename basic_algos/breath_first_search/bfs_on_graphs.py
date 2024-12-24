from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def bfs_graph(graph, start):
    visited = set()  # To track visited nodes
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        print(f"Visited {node}")

        # Add neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


# Example Problem
# Problem: Find the shorted path in an unweighted graph


def shortest_path(graph, start, target) -> int:
    visited = set()
    queue = deque([(start, 0)])  # (node, distance)

    while queue:
        node, distance = queue.popleft()

        if node == target:
            return distance

        if node in visited:
            continue

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return -1  # Target not reachable
