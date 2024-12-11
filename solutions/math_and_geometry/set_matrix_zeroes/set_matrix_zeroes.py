from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0

        if rowZero:
            for col in range(COLS):
                matrix[0][col] = 0

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
