# 110. Balanced Binary Tree

[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=QfJsau0ItOY&pp=ygUdbmVldGNvZGUgYmFsYW5jZWQgYmluYXJ5IHRyZWU%3D)

Given a binary tree, determine if it is
[height-balanced](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree).

> a height-balanced tree is a binary tree in which the left and right subtrees
> of
> <em>every</em> node differ in height by no more than 1.

**Example 1:**

<img src="./balanced_binary_tree.jpg" />

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**

```
Input: root = []
Output: true
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-104 <= Node.val <= 104`
