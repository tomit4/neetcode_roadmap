# 567. Permutation in String

[Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=UbyhOgBN834&pp=ygUebmVldGNvZGUgcGVybXV0YXRpb24gaW4gc3RyaW5n)

Given two strings `s1` and `s2`, return `true` if `s2` contains a
[permutation](https://en.wikipedia.org/wiki/Permutation) of `s1`, or `false`
otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of
`s2`.

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Constraints:**

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.
