from typing import Optional


def matrix_to_graph(adjList):
    if not adjList:
        return None

    nodes = {}
    for i in range(1, len(adjList) + 1):
        nodes[i] = Node(val=i)

    for i, neighbors in enumerate(adjList, start=1):
        nodes[i].neighbors = [nodes[neighbor] for neighbor in neighbors]

    return nodes[1]


def graph_to_matrix(node):
    if not node:
        return []

    visited = {}
    adjList = []

    def dfs(curr):
        if curr.val in visited:
            return
        visited[curr.val] = curr
        while len(adjList) < curr.val:
            adjList.append([])
        adjList[curr.val - 1] = [neighbor.val for neighbor in curr.neighbors]
        for neighbor in curr.neighbors:
            dfs(neighbor)

    dfs(node)
    return adjList


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        return


if __name__ == "__main__":
    solution = Solution()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = matrix_to_graph(adjList)
    clone = solution.cloneGraph(node=node)
    output = graph_to_matrix(clone)
    print(output)
    assert output == [[2, 4], [1, 3], [2, 4], [1, 3]]

    adjList = [[]]
    node = matrix_to_graph(adjList)
    clone = solution.cloneGraph(node=node)
    output = graph_to_matrix(clone)
    print(output)
    assert output == [[]]

    adjList = []
    node = matrix_to_graph(adjList)
    clone = solution.cloneGraph(node=node)
    output = graph_to_matrix(clone)
    print(output)
    assert output == []
