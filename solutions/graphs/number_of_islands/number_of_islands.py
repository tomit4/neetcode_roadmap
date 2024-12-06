from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def breath_first_search(row, col):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dir_row, dir_col in directions:
                    row, col = row + dir_row, col + dir_col
                    if (
                        (row) in range(rows)
                        and (col) in range(cols)
                        and grid[row][col] == "1"
                        and (row, col) not in visited
                    ):
                        queue.append((row, col))
                        visited.add((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    breath_first_search(row, col)
                    islands += 1

        return islands


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.numIslands(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
    )
    assert (
        solution.numIslands(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    print(
        solution.numIslands(
            grid=[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
    assert (
        solution.numIslands(
            grid=[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
