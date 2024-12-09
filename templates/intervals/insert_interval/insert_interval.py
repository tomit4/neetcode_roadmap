from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    assert solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [
        [1, 5],
        [6, 9],
    ]

    print(
        solution.insert(
            intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
        )
    )
    assert solution.insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
