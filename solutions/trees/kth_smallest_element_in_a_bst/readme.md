# 230. Kth Smallest Element in a BST

[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=5LUXSvjmGCw&pp=ygUmbmVldGNvZGUgS3RoIFNtYWxsZXN0IEVsZW1lbnQgSW4gYSBCc3Q%3D)

Given the root of a binary search tree, and an integer `k`, return the
`k`<sup>th</sup>
<em>smallest value (<b>1-indexed</b>) of all the values of the nodes in the
tree.</em>

**Example 1:**

<img src="./kth_smallest_element_in_a_bst_01.jpg" />

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2:**

<img src="./kth_smallest_element_in_a_bst_02.jpg" />

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`
