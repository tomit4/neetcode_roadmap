# 49. Group Anagrams

[Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)
[Neetcode Solution](https://www.youtube.com/watch?v=vzdNOK2oB2E&pp=ygUXbmVldGNvZGUgZ3JvdXAgYW5hZ3JhbXM%3D)

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Explanation:**

- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form
  each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
  form each other.

**Example 2:**

```
Input: strs = [""]

Output: [[""]]
```

**Example 3:**

```
Input: strs = ["a"]

Output: [["a"]]
```
