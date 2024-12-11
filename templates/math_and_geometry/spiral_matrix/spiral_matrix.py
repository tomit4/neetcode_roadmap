from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    assert solution.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]

    print(solution.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    assert solution.spiralOrder(
        matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
