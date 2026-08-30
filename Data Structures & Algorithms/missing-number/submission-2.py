class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        end = len(nums)
        sum_nums = int((0 + end) * (end + 1) / 2)
        return sum_nums - sum(nums)