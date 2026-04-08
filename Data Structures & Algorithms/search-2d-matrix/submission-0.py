class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for row in matrix:
            array.extend(row)

        l = 0
        r = len(array) - 1
        while l <= r:
            mid = (l + r) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False