class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if i != j:
                    output[j] *= num
                else:
                    continue

        return output
        