class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                return True
        return False