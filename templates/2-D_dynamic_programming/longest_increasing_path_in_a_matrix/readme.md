# 329. Longest Increasing Path in a Matrix

[Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=wCc_nd-GiEc&pp=ygUsbmVldGNvZGUgTG9uZ2VzdCBJbmNyZWFzaW5nIFBhdGggSW4gYSBNYXRyaXg%3D)

Given an `m x n` integers `matrix`, return <em>the length of the longest
increasing path in</em> `matrix`.

From each cell, you can either move in four directions: left, right, up, or
down. You <b>may not</b> move <b>diagonally</b> or move <b>outside the
boundary</b> (i.e., wrap-around is not allowed).

**Example 1:**

<img src="./longest_increasing_path_in_a_matrix_01.jpg" />

```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**

<img src="./longest_increasing_path_in_a_matrix_02.jpg" />

```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6].
Moving diagonally is not allowed.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: 1
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`
