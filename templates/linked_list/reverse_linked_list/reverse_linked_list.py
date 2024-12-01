from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper Function for converting an array to a linked list
def array_to_linked_list(arr: List) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current: ListNode = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return None


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list([1, 2, 3, 4, 5])
    reversed_head_1 = solution.reverseList(head_1)
    print(linked_list_to_array(reversed_head_1))

    head_2 = array_to_linked_list([1, 2])
    reversed_head_2 = solution.reverseList(head_2)
    print(linked_list_to_array(reversed_head_2))

    head_3 = array_to_linked_list([])
    reversed_head_3 = solution.reverseList(head_3)
    print(linked_list_to_array(reversed_head_3))
