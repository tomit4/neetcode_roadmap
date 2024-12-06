from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.countComponents(n=3, edges=[[0, 1], [0, 2]]))
    assert solution.countComponents(n=3, edges=[[0, 1], [0, 2]]) == 1

    print(solution.countComponents(n=6, edges=[[0, 1], [1, 2], [2, 3], [4, 5]]))
    assert solution.countComponents(n=6, edges=[[0, 1], [1, 2], [2, 3], [4, 5]]) == 2

    print(solution.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))
    assert solution.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]) == 2
