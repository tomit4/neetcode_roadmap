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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return None


if __name__ == "__main__":
    solution = Solution()
    list_1 = array_to_linked_list([1, 2, 4])
    list_2 = array_to_linked_list([1, 3, 4])
    merged_lists_1 = solution.mergeTwoLists(list_1, list_2)
    print(linked_list_to_array(merged_lists_1))
    assert linked_list_to_array(merged_lists_1) == [1, 1, 2, 3, 4, 4]

    list_3 = array_to_linked_list([])
    list_4 = array_to_linked_list([])
    merged_lists_2 = solution.mergeTwoLists(list_3, list_4)
    print(linked_list_to_array(merged_lists_2))
    assert linked_list_to_array(merged_lists_2) == []

    list_5 = array_to_linked_list([])
    list_6 = array_to_linked_list([0])
    merged_lists_3 = solution.mergeTwoLists(list_5, list_6)
    assert linked_list_to_array(merged_lists_3) == [0]
