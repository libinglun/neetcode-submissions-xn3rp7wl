# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        # reverse the linked list
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        # count the nth element
        if n == 1:
            tail = prev.next
        else:
            tail = prev
            last = prev
            cnt = 1
            while cnt < (n - 1):
                last = last.next
                cnt += 1

            last.next = last.next.next

        # reverse the linked list back
        after = None
        while tail:
            tmp = tail.next
            tail.next = after
            after = tail
            tail = tmp

        return after


        

        