class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ans = [0] * (n + 1)
        cost.append(0)
        ans[0] = cost[0]
        ans[1] = cost[1]
        for i in range(2, n + 1):
            ans[i] = cost[i] + min(ans[i - 1], ans[i - 2])

        return ans[-1]