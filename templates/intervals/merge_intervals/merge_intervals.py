from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    assert solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]

    print(solution.merge(intervals=[[1, 4], [4, 5]]))
    assert solution.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
