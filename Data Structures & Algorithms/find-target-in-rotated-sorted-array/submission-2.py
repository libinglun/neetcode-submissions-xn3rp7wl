class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[m] < nums[l]:
                # nums[m] < nums[l] implicitly
                if target > nums[r]:
                    # target greater than right bound, search left
                    r = m
                elif target < nums[m]:
                    r = m
                elif target > nums[m] and target <= nums[r]:
                    l = m + 1
            
            elif nums[m] >= nums[l] and nums[m] <= nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            elif nums[m] >= nums[l] and nums[m] >= nums[r]:
                # nums[l] > nums[r] implicitly
                if target > nums[m]:
                    l = m + 1
                elif target <= nums[m] and target >= nums[l]:
                    r = m
                elif target <= nums[r]:
                    l = m + 1
                else:
                    return -1

        return -1
        