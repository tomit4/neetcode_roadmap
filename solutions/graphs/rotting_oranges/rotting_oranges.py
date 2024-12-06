from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time = 0
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:  # found a fresh orange
                    fresh += 1
                if grid[row][col] == 2:  # found a rotting orange
                    queue.append([row, col])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:

            for _ in range(len(queue)):
                r, c = queue.popleft()
                for diff_row, diff_col in directions:
                    row, col = diff_row + r, diff_col + c
                    # if in bounds and fresh orange, make rotten
                    if (
                        row < 0
                        or row == len(grid)
                        or col < 0
                        or col == len(grid[0])
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2  # make rotten
                    queue.append([row, col])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    assert solution.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4

    print(solution.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    assert solution.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1

    print(solution.orangesRotting(grid=[[0, 2]]))
    assert solution.orangesRotting(grid=[[0, 2]]) == 0
