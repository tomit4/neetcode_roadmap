# 79. Word Search

[Word Search](https://leetcode.com/problems/word-search/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=pfiQ_PS1g8E&pp=ygUUbmVldGNvZGUgV29yZCBTZWFyY2g%3D)

Given an `m x n` grid of characters `board` and a string `word`, return `true`
if `word`
<em>exists in the grid.</em>

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

**Example 1:**

<img src="./word_search_01.jpg" />

```
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**

<img src="./word_search_02.jpg" />

```
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**

<img src="./word_search_03.jpg" />

```
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

**Constraints:**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.
