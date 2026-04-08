# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        start = head
        last_start = None
        while start:
            # find next k node:
            node = start
            cnt = 1
            while node.next and cnt < k:
                node = node.next
                cnt += 1

            if cnt < k:     # not enough for reverse
                last_start.next = start
                break
            # record next_start (4)
            next_start = node.next
            # reverse k node from start (inclusive)
            prev = None # placeholder, will be updated later by last start
            node = start
            for i in range(k):
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            
            if not last_start:
                head = prev

            # update last_start.next (1 -> 6)
            if last_start:
                last_start.next = prev
            # goto 4
            last_start = start
            start = next_start

        return head

