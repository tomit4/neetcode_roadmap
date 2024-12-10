# 62. Unique Paths

[Unique Paths](https://leetcode.com/problems/unique-paths/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=IlEsdxuD4lY&pp=ygUVbmVldGNvZGUgVW5pcXVlIFBhdGhz)

There is a robot on an `m x n` grid. The robot is initially located at the
<b>top-left corner</b> (i.e., `grid[0][0]`). The robot tries to move to the
<b>bottom-right corner</b> (i.e., `grid[m - 1][n - 1]`). The robot can only move
either down or right at any point in time.

Given the two integers `m` and `n`, return <em>the number of possible unique
paths that the robot can take to reach the bottom-right corner.</em>

The test cases are generated so that the answer will be less than or equal to
`2 * 10^9`.

**Example 1:**

<img src="./unique_paths.png" />

```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to
reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

**Constraints:**

- `1 <= m, n <= 100`
