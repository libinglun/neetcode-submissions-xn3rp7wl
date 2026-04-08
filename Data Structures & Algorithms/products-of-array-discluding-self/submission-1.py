class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' O(n^2) solution
        output = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if i != j:
                    output[j] *= num
                else:
                    continue

        return output
        '''

        # use the idea of prefix and suffix
        output = [1] * len(nums)
        prefix_product = 1
        for i in range(len(nums) - 1):
            prefix_product *= nums[i]
            output[i+1] *= prefix_product

        suffix_product = 1
        for i in range(len(nums) - 1, 0, -1):
            suffix_product *= nums[i]
            output[i-1] *= suffix_product

        return output


        