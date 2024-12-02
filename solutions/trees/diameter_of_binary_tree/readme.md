# 543. Diameter of Binary Tree

[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=bkxqA8Rfv04&pp=ygUgbmVldGNvZGUgZGlhbWV0ZXIgb2YgYmluYXJ5IHRyZWU%3D)

Given the `root` of a binary tree, return <em>the length of the diameter of the
tree.</em>

The <b>diameter</b> of a binary tree is the <b>length</b> of the longest path
between any two nodes in a tree. This path may or may not pass through the
`root`.

The <b>length</b> of a path between two nodes is represented by the number of
edges between them.

**Example 1:**

<img src="./diameter_of_binary_tree.jpg" />

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-100 <= Node.val <= 100`

<em>Hint:</em> Think of the problem as finding the sum of the maximum depth of
the left subtree and the maximum right subtree + 1 (the addition of + 1 is a
convention traditionally counting a NULL node adds a -1, which we need to negate
in this case...?)
