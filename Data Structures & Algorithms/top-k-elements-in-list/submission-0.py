class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        frequency = {k: v for k, v in sorted(count.items(), reverse=True, key=lambda item: item[1])}
        keys = list(frequency.keys())
        return keys[0:k]
        