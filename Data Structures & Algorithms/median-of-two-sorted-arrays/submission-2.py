class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # always keeps num1 as the smaller arragy
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        print(nums1, nums2)

        total = len(nums1) + len(nums2)
        half = total // 2

        # search for a x in nums1 and half-x elements in nums2
        l = 0
        r = len(nums1) - 1
        while True:
            m = (l + r) // 2        # index1
            j = half - (m + 1) - 1  # index2

            # no elements selected from nums1
            left1 = nums1[m] if m >= 0 else float("-inf")
            # nums1 all selected, but remain > 0
            right1 = nums1[m + 1] if (m + 1) < len(nums1) else float("inf")
            # j == -1 -> no elements in nums2 selected, all from nums1
            left2 = nums2[j] if j >= 0 else float('-inf')
            # 
            right2 = nums2[j + 1]

            print(left1, left2, right1, right2)
            print(l, r, m)
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2


            # find largest m such that nums1[m] <= nums2[j]
            elif left1 > right2:
                r = m - 1
            else:
                l = m + 1

            

