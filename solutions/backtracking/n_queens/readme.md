# 51. N-Queens

[N-Queens](https://leetcode.com/problems/n-queens/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=Ph95IHmRp5M&pp=ygURbmVldGNvZGUgTiBRdWVlbnM%3D)

The <b>n-queens</b> puzzle is the problem of placing `n` queens on an `n x n`
chessboard such that no two queens attack each other.

Given an integer `n`, return <em>all distinct solutions to the <b>n-queens
puzzle.<b></em> You may return the answer in <b>any order.</b>

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.

**Example 1:**

<img src="./n_queens.jpg" />

```
Input: n = 4
Output:
[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2:**

```
Input: n = 1
Output: [["Q"]]
```

**Constraints:**

- `1 <= n <= 9`
