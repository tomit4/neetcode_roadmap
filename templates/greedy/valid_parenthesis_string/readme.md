# 678. Valid Parenthesis String

[Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=QhPdNS143Qg&pp=ygUhbmVldGNvZGUgVmFsaWQgUGFyZW50aGVzaXMgU3RyaW5n)

Given a string `s` containing only three types of characters: '(', ')' and '*',
return `true` <em>if</em> `s` <em>is <b>valid</b>.</em>

The following rules define a <b>valid</b> string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left
  parenthesis '(' or an empty string "".

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "(*)"
Output: true
```

**Example 3:**

```
Input: s = "(*))"
Output: true
```

**Constraints:**

- `1 <= s.length <= 100`
- `s[i]` is '(', ')' or '*'.
