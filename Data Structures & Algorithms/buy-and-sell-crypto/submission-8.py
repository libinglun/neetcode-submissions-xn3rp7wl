class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        minprice = 1000
        profit = 0
        for p in prices:
            minprice = min(p, minprice)
            profit = max(profit, p - minprice)

        return profit
        '''

        # 1D-DP: dp[i] represents the best profit we can get if we sale on day i
        # dp[i] = prices[i] - min_price_till_i
        dp = [0] * len(prices)
        min_price = 10000000
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            dp[i] = max(dp[i], prices[i] - min_price)

        return max(dp)


        