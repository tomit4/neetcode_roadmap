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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return


if __name__ == "__main__":
    solution = Solution()
    list_1 = array_to_linked_list([1, 4, 5])
    list_2 = array_to_linked_list([1, 3, 4])
    list_3 = array_to_linked_list([2, 6])
    merged_k_list_1 = solution.mergeKLists([list_1, list_2, list_3])
    print(linked_list_to_array(merged_k_list_1))

    merged_k_list_2 = solution.mergeKLists([])
    print(linked_list_to_array(merged_k_list_2))

    list_4 = array_to_linked_list([])
    merged_k_list_3 = solution.mergeKLists([list_4])
    print(linked_list_to_array(merged_k_list_3))
