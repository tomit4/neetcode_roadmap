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
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeList(self, l1, l2):
        # todo
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


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
