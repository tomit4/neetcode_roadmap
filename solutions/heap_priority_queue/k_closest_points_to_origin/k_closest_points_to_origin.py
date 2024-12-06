import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest(points=[[1, 3], [-2, 2]], k=1))
    assert solution.kClosest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]]
    print(solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
    assert solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [
        [3, 3],
        [-2, 4],
    ]
