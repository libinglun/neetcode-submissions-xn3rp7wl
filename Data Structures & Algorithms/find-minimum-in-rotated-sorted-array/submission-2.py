class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            print(l, r)
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] >= nums[l] and nums[mid] < nums[r]:
                r = mid

        return nums[l]