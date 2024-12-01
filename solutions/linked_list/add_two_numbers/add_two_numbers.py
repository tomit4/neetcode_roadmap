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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        cur: ListNode = dummy

        carry: int = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val: int = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # updating pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    l1 = array_to_linked_list([2, 4, 3])
    l2 = array_to_linked_list([5, 6, 4])
    add_two_numbers_1 = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_array(add_two_numbers_1))

    l3 = array_to_linked_list([0])
    l4 = array_to_linked_list([0])
    add_two_numbers_2 = solution.addTwoNumbers(l3, l4)
    print(linked_list_to_array(add_two_numbers_2))

    l5 = array_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l6 = array_to_linked_list([9, 9, 9, 9])
    add_two_numbers_3 = solution.addTwoNumbers(l5, l6)
    print(linked_list_to_array(add_two_numbers_3))
