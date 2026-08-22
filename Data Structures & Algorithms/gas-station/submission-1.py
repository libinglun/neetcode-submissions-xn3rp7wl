class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:   
        if sum(gas) < sum(cost):
            return -1
        diff = [ gas[i] - cost[i] for i in range(len(gas))]
        total = 0

        ans = 0
        for i in range(len(gas)):
            total += diff[i]
            if total <= 0:
                ans = i + 1
                total = 0

        return ans % len(gas)
            
        