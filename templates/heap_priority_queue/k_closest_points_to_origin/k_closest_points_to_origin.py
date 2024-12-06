from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest(points=[[1, 3], [-2, 2]], k=1))
    assert solution.kClosest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]]
    print(solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
    assert solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [
        [3, 3],
        [-2, 4],
    ]
