class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        for i, l in enumerate(s):
            lastIndex[l] = i

        res = []
        length = 0
        end = 0
        for i, l in enumerate(s):
            length += 1
            end = max(end, lastIndex[l])
            if i == end:
                res.append(length)
                length = 0

        return res
            
            