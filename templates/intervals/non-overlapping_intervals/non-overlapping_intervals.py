from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
    assert (
        solution.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    )

    print(solution.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))
    assert solution.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2

    print(solution.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))
    assert solution.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]) == 0
