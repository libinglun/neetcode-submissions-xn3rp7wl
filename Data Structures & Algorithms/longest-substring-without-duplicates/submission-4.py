class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        ans = 0
        '''
        for i in range(len(s)):
            if s[i] not in string:
                string += s[i]
                ans = max(ans, len(string))
            else:
                # can use a while function to remove the first element until s[i] is removed
                index = string.find(s[i])
                string = string[index+1:] + s[i]

        return ans
        '''
        string = ""
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in string:
                string += s[r]
                ans = max(ans, len(string))
            else:
                l = string.find(s[r])
                string = string[l + 1:] + s[r]
            r += 1

        return ans