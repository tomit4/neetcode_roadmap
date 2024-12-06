from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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
