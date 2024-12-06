# 130. Surrounded Regions

[Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=9z2BunfoZ5Y&pp=ygUbbmVldGNvZGUgU3Vycm91bmRlZCBSZWdpb25z)

You are given an `m x n` matrix board containing <b>letters</b> 'X' and 'O',
<b>capture regions</b> that are <b>surrounded</b>:

- <b>Connect</b>: A cell is connected to adjacent cells horizontally or
  vertically.
- <b>Region</b>: To form a region <b>connect every</b> 'O' cell.
- <b>Surround</b>: The region is surrounded with 'X' cells if you can <b>connect
  the region</b> with 'X' cells and none of the region cells are on the edge of
  the board.

A <b>surrounded region is captured</b> by replacing all 'O's with 'X's in the
input matrix board.

**Example 1:**

```
Input: board =
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output:
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
```

**Explanation:**

<img src="./surrounded_regions.jpg" />

In the above diagram, the bottom region is not captured because it is on the
edge of the board and cannot be surrounded.

**Example 2:**

```
Input: board = [["X"]]

Output: [["X"]]
```

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is 'X' or 'O'.
