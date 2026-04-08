# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1

        print('length: ', length)

        half = length // 2
        cnt = 0
        first = head
        while cnt < half:
            first = first.next
            cnt += 1

        second = first.next
        first.next = None

        # reverse the second half link list
        last = None
        while second:
            tmp = second.next
            second.next = last
            last = second
            second = tmp
        
        while last is not None:
            print(head.val, last.val)
            tmp_head = head.next
            tmp_last = last.next
            head.next = last
            last.next = tmp_head
            head = tmp_head
            last = tmp_last
        


        


        