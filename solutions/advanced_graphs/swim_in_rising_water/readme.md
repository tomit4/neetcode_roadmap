# 778. Swim in Rising Water

[Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=amvrKlMLuGY&pp=ygUdbmVldGNvZGUgU3dpbSBJbiBSaXNpbmcgV2F0ZXI%3D)

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]`
represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere is `t`.
You can swim from a square to another 4-directionally adjacent square if and
only if the elevation of both squares individually are at most `t`. You can swim
infinite distances in zero time. Of course, you must stay within the boundaries
of the grid during your swim.

Return <em>the least time until you can reach the bottom right square</em>
`(n - 1, n - 1)` <em>if you start at the top left square</em> `(0, 0)`.

**Example 1:**

<img src="./swim_in_rising_water_01.jpg" />

```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0). You cannot go anywhere else because
4-directionally adjacent neighbors have a higher elevation than t = 0. You cannot
reach point (1, 1) until time 3. When the depth of water is 3, we can swim anywhere
inside the grid.
```

**Example 2:**

<img src="./swim_in_rising_water_02.jpg" />

```
Input: grid =
[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```

**Constraints:**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value `grid[i][j]` is <b>unique</b>.
