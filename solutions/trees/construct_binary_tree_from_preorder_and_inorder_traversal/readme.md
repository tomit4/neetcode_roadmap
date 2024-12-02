# 105. Construct Binary Tree from Preorder and Inorder Traversal

[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=ihj4IQGZ2zc&pp=ygVCbmVldGNvZGUgQ29uc3RydWN0IEJpbmFyeSBUcmVlIEZyb20gUHJlb3JkZXIgQW5kIElub3JkZXIgVHJhdmVyc2Fs)

Given two integer arrays `preorder` and `inorder` where `preorder` is the
preorder traversal of a binary tree and `inorder` is the inorder traversal of
the same tree, construct and return <em>the binary tree.</em>

**Example 1:**

<img src="./construct_binary_search_tree_from_preorder_and_inorder_traversal.jpg" />

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

**Constraints:**

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of <b>unique</b> values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is <b>guaranteed</b> to be the preorder traversal of the tree.
- `inorder` is <b>guaranteed</b> to be the inorder traversal of the tree.
