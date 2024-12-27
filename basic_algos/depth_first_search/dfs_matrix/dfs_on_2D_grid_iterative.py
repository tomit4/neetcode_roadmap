def dfs_grid_iterative(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(start_r, start_c):
        stack = [(start_r, start_c)]

        while stack:
            r, c = stack.pop()

            if (
                (r, c) in visited
                or r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or grid[r][c] == 0
            ):
                return

            visited.add((r, c))  # Mark as visited
            print(f"Visiting cell ({r}, {c})")

            # Add neighbors (up, down, left, right)
            stack.append((r - 1, c))  # Up
            stack.append((r + 1, c))  # Down
            stack.append((r, c - 1))  # Left
            stack.append((r, c + 1))  # Right

    # Start DFS for each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                print(f"Starting new DFS from ({r}, {c})")
                dfs(r, c)
