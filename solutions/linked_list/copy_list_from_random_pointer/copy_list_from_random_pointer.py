from __future__ import annotations

from typing import Dict, List, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Helper Function for converting an array to a linked list
def array_to_linked_list(arr: List) -> Optional[Node]:
    if not arr:
        return None
    nodes = [Node(val) for val, _ in arr]

    for i, (_, random_index) in enumerate(arr):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


# Helper function that converts a linked list to an array
def linked_list_to_array(head: Node | None):
    if not head:
        return []

    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1

    result = []
    current = head
    while current:
        random_index = node_to_index.get(current.random, None)
        result.append([current.val, random_index])
        current = current.next

    return result


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_to_copy: Dict[Node | None, Node | None] = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]  # type: ignore
            copy.random = old_to_copy[cur.random]  # type: ignore
            cur = cur.next

        return old_to_copy[head]


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copied_random_list_1 = solution.copyRandomList(head_1)
    print(linked_list_to_array(copied_random_list_1))

    head_2 = array_to_linked_list([[1, 1], [2, 1]])
    copied_random_list_2 = solution.copyRandomList(head_2)
    print(linked_list_to_array(copied_random_list_2))

    head_3 = array_to_linked_list([[3, None], [3, 0], [3, None]])
    copied_random_list_3 = solution.copyRandomList(head_3)
    print(linked_list_to_array(copied_random_list_3))
