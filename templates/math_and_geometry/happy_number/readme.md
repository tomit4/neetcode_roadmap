# 202. Happy Number

[Happy Number](https://leetcode.com/problems/happy-number/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=ljz85bxOYJ0&pp=ygUVbmVldGNvZGUgSGFwcHkgTnVtYmVy)

Write an algorithm to determine if a number `n` is happy.

A <b>happy number</b> is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the
  squares of its digits.
- Repeat the process until the number equals `1` (where it will stay), or it
  <b>loops endlessly in a cycle</b> which does not include `1`.
- Those numbers for which this process <b>ends in 1</b> are happy.

Return `true` <em>if</em> `n` <em>is a happy number, and</em> `false`<em> if
not.</em>

**Example 1:**

```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

**Example 2:**

```
Input: n = 2
Output: false
```

**Constraints:**

- `1 <= n <= 2^31 - 1`
