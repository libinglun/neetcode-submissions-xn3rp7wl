class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i, num in enumerate(nums):
            if num in remain:
                return [remain[num], i]
            if target - num not in remain:
                remain[target-num] = i
            
            
        