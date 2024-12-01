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
        dummy: ListNode = ListNode()
        tail: ListNode = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    list_1 = array_to_linked_list([1, 2, 4])
    list_2 = array_to_linked_list([1, 3, 4])
    merged_lists_1 = solution.mergeTwoLists(list_1, list_2)
    print(linked_list_to_array(merged_lists_1))

    list_3 = array_to_linked_list([])
    list_4 = array_to_linked_list([])
    merged_lists_2 = solution.mergeTwoLists(list_3, list_4)
    print(linked_list_to_array(merged_lists_2))

    list_5 = array_to_linked_list([])
    list_6 = array_to_linked_list([0])
    merged_lists_3 = solution.mergeTwoLists(list_5, list_6)
    print(linked_list_to_array(merged_lists_3))
