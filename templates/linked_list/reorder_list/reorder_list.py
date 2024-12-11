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
    def reorderList(self, head: Optional[ListNode]) -> None:
        return None


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list([1, 2, 3, 4])
    solution.reorderList(head_1)
    print(linked_list_to_array(head_1))
    assert linked_list_to_array(head_1) == [1, 4, 2, 3]

    head_2 = array_to_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head_2)
    print(linked_list_to_array(head_2))
    assert linked_list_to_array(head_2) == [1, 5, 2, 4, 3]
