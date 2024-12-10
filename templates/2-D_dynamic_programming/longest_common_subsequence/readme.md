# 1143. Longest Common Subsequence

[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=Ua0GhsJSlWM&pp=ygUjbmVldGNvZGUgTG9uZ2VzdCBDb21tb24gU3Vic2VxdWVuY2U%3D)

Given two strings `text1` and `text2`, return <em>the length of their longest
<b>common subsequence.</b></em> If there is no <b>common subsequence</b>, return
`0`.

A <b>subsequence</b> of a string is a new string generated from the original
string with some characters (can be none) deleted without changing the relative
order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A <b>common subsequence</b> of two strings is a subsequence that is common to
both strings.

**Example 1:**

```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

**Example 2:**

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

**Example 3:**

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

**Constraints:**

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.
