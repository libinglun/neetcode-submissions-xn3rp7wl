class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use negation at index n-1 to label n is contained
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            nums[abs(num) - 1] *= -1


        # use a hashset to record every integer -- space complexity O(n)
        '''
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return num
        '''
        