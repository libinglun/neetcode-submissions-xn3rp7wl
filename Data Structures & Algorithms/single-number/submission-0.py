class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # XOR: x ^ x = 0; x ^ 0 = x
        for num in nums:
            res = num ^ res

        return res