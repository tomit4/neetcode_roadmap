from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper Function for converting an array to a linked list
def array_to_linked_list(arr: List, pos: int) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current: ListNode = head
    nodes = [head]
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
        nodes.append(current)

    if pos != -1:
        current.next = nodes[pos]
    return head


# Helper function that converts a linked list to an array
def linked_list_to_array(head: ListNode | None):
    arr: List[int] = []
    current: ListNode | None = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # type:ignore
            fast = fast.next.next
            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list(arr=[3, 2, 0, -4], pos=1)
    head_has_cycle_1 = solution.hasCycle(head_1)
    print(head_has_cycle_1)

    head_2 = array_to_linked_list(arr=[1, 2], pos=0)
    head_has_cycle_2 = solution.hasCycle(head_2)
    print(head_has_cycle_2)

    head_3 = array_to_linked_list(arr=[1], pos=-1)
    head_has_cycle_3 = solution.hasCycle(head_3)
    print(head_has_cycle_3)
