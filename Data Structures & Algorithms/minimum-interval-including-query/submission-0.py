class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        minheap = []
        j = 0

        for q, i in sorted_queries:
            
            # add all intervals that start before the query into priority queue
            while j < len(intervals) and intervals[j][0] <= q:
                start, end = intervals[j]
                length = end - start + 1
                heapq.heappush(minheap, (length, end))
                j += 1

            # remove those intervals end before the query
            # note that this is lazy deletion
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                res[i] = minheap[0][0]

        return res
            