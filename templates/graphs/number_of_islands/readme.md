# 200. Number of Islands

[Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=pV2kpPD66nE&pp=ygUabmVldGNvZGUgTnVtYmVyIG9mIElzbGFuZHM%3D)

Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and
'0's (water), return <em>the number of islands.</em>

An <b>island</b> is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

**Example 1:**

```
Input:
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is '0' or '1'.
