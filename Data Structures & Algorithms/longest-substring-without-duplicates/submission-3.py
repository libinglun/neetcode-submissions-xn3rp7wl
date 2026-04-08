class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        ans = 0
        for i in range(len(s)):
            if s[i] not in string:
                string += s[i]
                ans = max(ans, len(string))
            else:
                index = string.find(s[i])
                string = string[index+1:] + s[i]

        return ans