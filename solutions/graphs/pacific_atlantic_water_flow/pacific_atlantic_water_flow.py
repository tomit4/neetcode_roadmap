from typing import List
from warnings import warn


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def depth_first_search(row, col, visited, prev_height):
            if (
                (row, col) in visited
                or row < 0
                or col < 0
                or row == ROWS
                or col == COLS
                or heights[row][col] < prev_height
            ):
                return
            visited.add((row, col))
            depth_first_search(row + 1, col, visited, heights[row][col])
            depth_first_search(row - 1, col, visited, heights[row][col])
            depth_first_search(row, col + 1, visited, heights[row][col])
            depth_first_search(row, col - 1, visited, heights[row][col])

        for col in range(COLS):
            depth_first_search(0, col, pacific, heights[0][col])
            depth_first_search(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

        for row in range(ROWS):
            depth_first_search(row, 0, pacific, heights[row][0])
            depth_first_search(row, COLS - 1, atlantic, heights[row][COLS - 1])

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.pacificAtlantic(
            heights=[
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    )
    assert solution.pacificAtlantic(
        heights=[
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    ) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    print(solution.pacificAtlantic(heights=[[1]]))
    assert solution.pacificAtlantic(heights=[[1]]) == [[0, 0]]
