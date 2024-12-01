from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
        )
    )
    print(
        solution.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
        )
    )
