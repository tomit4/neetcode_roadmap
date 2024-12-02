# 98. Validate Binary Search Tree

[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=s6ATEkipzow&pp=ygUkbmVldGNvZGUgVmFsaWRhdGUgQmluYXJ5IFNlYXJjaCBUcmVl)

Given the `root` of a binary tree, <em>determine if it is a valid binary search
tree (BST)</em>.

A <b>valid BST</b> is defined as follows:

- The left [subtree](https://en.wikipedia.org/wiki/Tree_(abstract_data_type)) of
  a node contains only nodes with keys <b>less than</b> the node's key.
- The right subtree of a node contains only nodes with keys <b>greater than</b>
  the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

<img src="./validate_binary_search_tree_01.jpg" />

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

<img src="./validate_binary_search_tree_02.jpg" />

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-231 <= Node.val <= 231 - 1`
