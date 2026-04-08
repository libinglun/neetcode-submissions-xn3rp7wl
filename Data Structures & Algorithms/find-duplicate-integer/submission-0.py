class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use a hashset to record every integer -- space complexity O(n)
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return num
        