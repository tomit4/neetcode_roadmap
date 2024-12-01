# 143. Reorder List

[Reorder List](https://leetcode.com/problems/reorder-list/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=S5bfdUTrKLM&pp=ygUVbmVldGNvZGUgcmVvcmRlciBsaXN0)

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

<em>Reorder the list to be on the following form:</em>

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be
changed.

**Example 1:**

<img src="./reorder_list_01.jpg" />

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

Example 2:

<img src="./reorder_list_02.jpg" />

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Constraints:**

- The number of nodes in the list is in the range `[1, 5 * 104]`.
- `1 <= Node.val <= 1000`
