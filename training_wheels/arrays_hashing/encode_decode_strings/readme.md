# 659 Encode and Decode Strings

[Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode)

[Neetcode Solution](https://www.youtube.com/watch?v=B1k_sxOSgv8&pp=ygUibmVldGNvZGUgZW5jb2RlIGFuZCBkZWNvZGUgc3RyaW5ncw%3D%3D)

Design an algorithm to encode a list to a string. The encoded string is then
sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`.

**Example 1:**

```
Input: ["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you"]
```

**Example 2:**

```
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
```

**Constraints:**

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `[strs[i]]` contains only UTF-8 characters

**Explanation:**

One possible encode method is "lint:;code:;love:;you"
