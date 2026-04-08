# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        last = None
        while node is not None:
            tmp = node.next
            node.next = last
            last = node
            node = tmp

        return last
        
        