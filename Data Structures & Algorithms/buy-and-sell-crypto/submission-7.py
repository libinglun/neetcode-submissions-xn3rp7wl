class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 1000
        profit = 0
        for p in prices:
            minprice = min(p, minprice)
            profit = max(profit, p - minprice)

        return profit


        