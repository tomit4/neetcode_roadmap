from collections import deque

grid = [[1, 1, 0], [0, 1, 0], [1, 0, 0]]


def bfs_grid(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))

        while queue:
            r, c = queue.popleft()
            print(f"Visiting cell ({r}, {c})")

            # Explore neighbors (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] == 1
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        bfs(r, c)


# Example Problem
# Problem: Count the number of islands in a grid.


def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] == "1"
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands
