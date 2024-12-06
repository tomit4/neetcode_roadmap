from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find Algorithm
        parents = [i for i in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)

        def find(node):
            parent = parents[node]

            while parent != parents[parent]:
                parent = parents[parents[parent]]
                parent = parents[parent]

            return parent

        # return False if can't complete
        def union(node_1, node_2):
            parent_1, parent_2 = find(node_1), find(node_2)

            if parent_1 == parent_2:
                return False

            if ranks[parent_1] > ranks[parent_2]:
                parents[parent_2] = parent_1
                ranks[parent_1] = ranks[parent_2]
            else:
                parents[parent_1] = parent_2
                ranks[parent_2] = ranks[parent_1]

            return True

        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                return [node_1, node_2]
        # Should never execute
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]]))
    assert solution.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]]) == [2, 3]

    print(
        solution.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    )
    assert solution.findRedundantConnection(
        edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    ) == [1, 4]
