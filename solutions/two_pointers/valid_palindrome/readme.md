# 125. Valid Palindrome

[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=jJXJ16kPFWg&pp=ygUZbmVldGNvZGUgdmFsaWQgcGFsaW5kcm9tZQ%3D%3D)

A phrase is a <b>palindrome</b> if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` <em>if it is a <b>palindrome</b>, or false
otherwise</em>.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**

- `1 <= s.length <= 2 * 105`
- `s` consists only of printable ASCII characters.
