# 76. Minimum Window Substring

[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)

[Neetcode Solutioin](https://www.youtube.com/watch?v=jSto0O4AJbM&pp=ygUhbmVldGNvZGUgbWluaW11bSB3aW5kb3cgc3Vic3RyaW5n)

Given two strings `s` and `t` of lengths `m` and `n` respectively, return
<em>the <b>minimum window
[substring](https://en.wikipedia.org/wiki/Substring)</b> of</em> `s` <em>such
that every character in</em> `t` <em>(<b>including duplicates</b>) is included
in the window</em>. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is <b>unique</b>.

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s
only has one 'a', return empty string.
```

**Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` and `t` consist of uppercase and lowercase English letters.
