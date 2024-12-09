from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            not_overlapping = start >= prev_end
            if not_overlapping:
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)

        return res


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
