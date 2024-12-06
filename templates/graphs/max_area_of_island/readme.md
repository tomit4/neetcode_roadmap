# 695. Max Area of Island

[Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=iJGr1OtmH0c&pp=ygUbbmVldGNvZGUgTWF4IEFyZWEgb2YgSXNsYW5k)

You are given an `m x n` binary matrix `grid`. An island is a group of 1's
(representing land) connected <b>4-directionally</b> (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The <b>area</b> of an island is the number of cells with a value `1` in the
island.

Return <em>the maximum <b>area</b> of an island in<em> `grid`. If there is no
island, return `0`.

**Example 1:**

<img src="./max_area_of_island.jpg" />

```
Input:
grid =
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.
