# 74. Search a 2D Matrix

[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=Ber2pi2C0j0&pp=ygUbbmVldGNvZGUgc2VhcmNoIGEgMmQgbWF0cml4)

You are given an `m x n` integer matrix `matrix` with the following two
properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous
  row.

Given an integer `target`, return `true` <em>if</em> `target` <em>is in</em>
`matrix` <em>or</em> `false` <em>otherwise</em>.

You must write a solution in $O(log(m * n))$ time complexity.

**Example 1:**

<img src="./search_a_2d_matrix_01.jpg" />

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**

<img src="./search_a_2d_matrix_02.jpg" />

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-104 <= matrix[i][j], target <= 104`
