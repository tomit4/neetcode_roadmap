from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.minInterval(
            intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5]
        )
    )
    assert solution.minInterval(
        intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5]
    ) == [3, 3, 1, 4]

    print(
        solution.minInterval(
            intervals=[[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22]
        )
    )
    assert solution.minInterval(
        intervals=[[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22]
    ) == [2, -1, 4, 6]