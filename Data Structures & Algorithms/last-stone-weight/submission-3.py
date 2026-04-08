import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxheap = stones
        heapq.heapify_max(maxheap)
        while len(maxheap) >= 2:
            x = heapq.heappop_max(maxheap)
            y = heapq.heappop_max(maxheap)
            print(x, y)

            if x == y:
                continue
            else:
                heapq.heappush_max(maxheap, abs(x - y))

        if len(maxheap):
            return heapq.heappop(maxheap)
        return 0
