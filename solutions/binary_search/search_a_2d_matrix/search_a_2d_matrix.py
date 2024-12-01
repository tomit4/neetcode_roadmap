from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        top: int = 0
        bottom: int = ROWS - 1

        while top <= bottom:
            middle_row: int = (top + bottom) // 2
            if target > matrix[middle_row][-1]:
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            else:
                break

        if not (top <= bottom):
            return False

        middle_row = (top + bottom) // 2
        left: int = 0
        right: int = COLS - 1
        while left <= right:
            middle_point: int = (left + right) // 2
            if target > matrix[middle_row][middle_point]:
                left = middle_point + 1
            elif target < matrix[middle_row][middle_point]:
                right = middle_point - 1
            else:
                return True

        return False


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
