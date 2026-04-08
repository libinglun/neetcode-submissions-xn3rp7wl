class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = [0] * 26
        for char in s1:
            idx = ord(char) - ord('a')
            count[idx] += 1

        count2 = [0] * 26
        for i in range(len(s1)):
            idx = ord(s2[i]) - ord('a')
            count2[idx] += 1
        if count2 == count:
            return True

        for i in range(len(s2) - len(s1)):
            count2[ord(s2[i]) - ord('a')] -= 1
            count2[ord(s2[i + len(s1)]) - ord('a')] += 1
            if count2 == count:
                return True

        return False
        

        
        