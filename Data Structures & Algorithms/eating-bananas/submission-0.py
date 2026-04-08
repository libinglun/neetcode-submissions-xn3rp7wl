class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = float('inf')

        while l <= r:
            print(l, r)
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += -(-p // m)
            print(hours)
            if hours > h:
                l = m + 1
            if hours <= h:
                # too fast, decrease k to slow down 
                min_k = m
                r = m - 1

        return min_k

        