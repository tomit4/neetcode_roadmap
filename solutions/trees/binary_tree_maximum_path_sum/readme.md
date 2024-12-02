# 124. Binary Tree Maximum Path Sum

[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=Hr5cWUld4vU&pp=ygUlbmVldGNvZGUgQmluYXJ5IFRyZWUgTWF4aW11bSBQYXRoIFN1bQ%3D%3D)

A <b>path</b> in a binary tree is a sequence of nodes where each pair of
adjacent nodes in the sequence has an edge connecting them. A node can only
appear in the sequence <b>at most once.</b> Note that the path does not need to
pass through the root.

The <b>path sum</b> of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return <em>the maximum <b>path sum</b> of any
<b>non-empty</b> path.</em>

**Example 1:**

<img src="./binary_tree_maximum_path_sum_01.jpg" />

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2:**

<img src="./binary_tree_maximum_path_sum_02.jpg" />

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`
