class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers since the list is sorted!
        index1, index2 = 0, len(numbers) - 1
        while index1 < index2:
            nsum = numbers[index1] + numbers[index2]
            if nsum == target:
                return [index1 + 1, index2 + 1]
            elif nsum > target:
                index2 -= 1
            else:
                index1 += 1
        '''brute force
        for i in range(len(numbers)):
            remain = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[j] == remain:
                    return [i+1, j+1]
        '''
        