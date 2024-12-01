# 25. Reverse Nodes in k-Group

[Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=1UOPsfP85V4&pp=ygUhbmVldGNvZGUgcmV2ZXJzZSBub2RlcyBpbiBrIGdyb3Vw)

Given the `head` of a linked list, reverse the nodes of the list `k` at a time,
and return <em>the modified list.</em>

`k` is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of `k` then left-out nodes, in
the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be
changed.

**Example 1:**

<img src="./reverse_nodes_in_k-group_01.jpg" />

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

<img src="./reverse_nodes_in_k-group_02.jpg" />

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`
