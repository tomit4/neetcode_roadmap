from collections import defaultdict
from typing import List


# establish default dictionaries of sets for rows and cols and squares
# double for loop over entire board
# if '.' encountered, continue next iteration of loop
# if element is in rows dictionary set
# or if element is in cols dictionary set
# determine which 3x3 square your element is in by dividing row and column each by 3
# and then check if  element is in squares dictionary set
# return false if any are in their sets
# otherwise add element to cols, rows, and squares dictionary set
# return True if loops finish
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    board_1: List[List[str]] = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.isValidSudoku(board=board_1))
    assert solution.isValidSudoku(board=board_1) == True

    board_2: List[List[str]] = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.isValidSudoku(board=board_2))
    assert solution.isValidSudoku(board=board_2) == False
