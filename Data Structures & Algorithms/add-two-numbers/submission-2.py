# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2

        head = ans = ListNode(0, None)
        carry = 0
        while node1 or node2 or carry > 0:

            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0

            val = val1 + val2 + carry
            carry = 0
            if val >= 10:
                carry = 1
                val = val % 10

            ans.next = ListNode(val)

            ans = ans.next
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next

        return head.next


