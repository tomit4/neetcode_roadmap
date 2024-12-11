# 73. Set Matrix Zeroes

[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=T41rL0L3Pnw&pp=ygUabmVldGNvZGUgU2V0IE1hdHJpeCBaZXJvZXM%3D)

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire
row and column to `0`'s.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

**Example 1:**

<img src="./set_matrix_zeroes_01.jpg" />

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

<img src="./set_matrix_zeroes_02.jpg" />

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
