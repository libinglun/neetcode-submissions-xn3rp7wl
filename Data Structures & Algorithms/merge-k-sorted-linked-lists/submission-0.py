# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if not k:
            return None

        ans = head = ListNode(0)
        
        while True:
            empty = 0
            min_val = float('inf')
            min_index = -1
            for i in range(k):
                if not lists[i]:
                    empty += 1
                    continue
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i

            if empty == k:
                break
            print(min_val, min_index)

            head.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            head = head.next
        
        return ans.next


            

