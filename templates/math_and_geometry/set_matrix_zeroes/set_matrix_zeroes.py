from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        return None


if __name__ == "__main__":
    solution = Solution()
    matrix_1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix=matrix_1)
    print(matrix_1)
    assert matrix_1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix_2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(matrix=matrix_2)
    print(matrix_2)
    assert matrix_2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
