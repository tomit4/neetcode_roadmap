# 141. Linked List Cycle

[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=gBTe7lFR3vc&pp=ygUabmVldGNvZGUgbGlua2VkIGxpc3QgY3ljbGU%3D)

Given `head`, the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's `next` pointer is connected to.
<b>Note that</b> `pos` <b>is not passed as a parameter.</b>

Return `true` <em>if there is a cycle in the linked list.</em> Otherwise, return
`false`.

**Example 1:**

<img src="./linked_list_cycle_01.png" />

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st
node (0-indexed).
```

**Example 2:**

<img src="./linked_list_cycle_02.png" />

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th
node.
```

**Example 3:**

<img src="./linked_list_cycle_03.png" />

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 104]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a <b>valid index</b> in the linked-list.
