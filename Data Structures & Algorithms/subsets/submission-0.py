class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):
            # & is bit-wise AND. E.g. i = 5 = 101 & 100 = 4 > 0
            subset = [nums[j] for j in range(n) if i & (1 << j)]
            res.append(subset)

        return res