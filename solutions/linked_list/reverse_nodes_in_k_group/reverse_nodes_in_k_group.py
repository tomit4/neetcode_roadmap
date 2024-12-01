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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(0, head)
        group_prev: ListNode = dummy

        while True:
            kth: ListNode | None = self.getKth(group_prev, k)
            if not kth:
                break
            group_next: ListNode | None = kth.next

            #  reverse group
            prev: ListNode | None = kth.next
            curr: ListNode | None = group_prev.next

            while curr != group_next:
                tmp = curr.next  # type:ignore
                curr.next = prev  # type:ignore
                prev = curr
                curr = tmp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp  # type:ignore

        return dummy.next

    def getKth(self, curr: ListNode | None, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


if __name__ == "__main__":
    solution = Solution()
    head_1 = array_to_linked_list([1, 2, 3, 4, 5])
    reversed_k_group_1 = solution.reverseKGroup(head=head_1, k=2)
    print(linked_list_to_array(reversed_k_group_1))

    head_2 = array_to_linked_list([1, 2, 3, 4, 5])
    reversed_k_group_2 = solution.reverseKGroup(head=head_2, k=3)
    print(linked_list_to_array(reversed_k_group_2))
