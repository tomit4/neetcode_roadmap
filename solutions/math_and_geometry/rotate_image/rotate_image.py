from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save the topLeft value
                topLeft = matrix[top][left + i]

                # move the bottom left into the top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into botttom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1

        return None


if __name__ == "__main__":
    solution = Solution()
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix=matrix_1)
    print(matrix_1)
    assert matrix_1 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    matrix_2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix=matrix_2)
    print(matrix_2)
    assert matrix_2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
