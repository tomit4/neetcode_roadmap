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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return None


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list([1, 2, 3, 4, 5])
    list_with_n_removed_1 = solution.removeNthFromEnd(head=head_1, n=2)
    print(linked_list_to_array(list_with_n_removed_1))
    assert linked_list_to_array(list_with_n_removed_1) == [1, 2, 3, 5]

    head_2 = array_to_linked_list([1])
    list_with_n_removed_2 = solution.removeNthFromEnd(head=head_2, n=1)
    print(linked_list_to_array(list_with_n_removed_2))
    assert linked_list_to_array(list_with_n_removed_2) == []

    head_3 = array_to_linked_list([1, 2])
    list_with_n_removed_3 = solution.removeNthFromEnd(head=head_3, n=1)
    print(linked_list_to_array(list_with_n_removed_3))
    assert linked_list_to_array(list_with_n_removed_3) == [1]
