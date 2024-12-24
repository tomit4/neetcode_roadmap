# A 2D grid isn't explicitly represented by GraphNode objects, Instead:
# - Each cell is treated as a "node"
# - Neighbors are adjacent cells (up, down, left, right, sometimes diagonals).

# Example grid
# Consider this simple grid
# 1 1 0
# 0 1 0
# 1 0 0

# We want to explore all connected 1s starting from any given 1. This is a common DFS use case.

# Generic Problem: Count All Connected 1s in the Gridf


def dfs_grid_recursive(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or (r, c) in visited
            or grid[r][c] == 0
        ):
            return

        # Mark the current cell as visited
        visited.add((r, c))

        # Process the current cell
        print(f"Visiting cell ({r}, {c})")

        # Explore neighbors (up, down, left, right)
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

        # Start DFS on each cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    print(f"Starting new DFS from ({r}, {c})")
                    dfs(r, c)  # Perform DFS for connected component
