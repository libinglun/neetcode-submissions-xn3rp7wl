class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        # Sort
        '''
        frequency = {k: v for k, v in sorted(count.items(), reverse=True, key=lambda item: item[1])}
        keys = list(frequency.keys())
        return keys[0:k]
        '''
        # Min Heap:
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)     # pop out the num with the least frequency
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        