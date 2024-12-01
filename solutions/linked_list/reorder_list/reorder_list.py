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
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next  # type:ignore

        while fast and fast.next:
            slow = slow.next  # type:ignore
            fast = fast.next.next

        second = slow.next  # type:ignore
        slow.next = None  # type:ignore

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs of list
        first = head
        second = prev
        while second:
            tmp1 = first.next  # type:ignore
            tmp2 = second.next
            first.next = second  # type:ignore
            second.next = tmp1
            first = tmp1
            second = tmp2

        print(linked_list_to_array(head))


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list([1, 2, 3, 4])
    solution.reorderList(head_1)

    head_2 = array_to_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head_2)
