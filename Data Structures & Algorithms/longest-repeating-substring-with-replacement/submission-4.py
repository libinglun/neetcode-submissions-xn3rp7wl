class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        r = 0
        ans = r - l
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while sum(freq.values()) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            print(freq, r, l)
            ans = max(ans, r - l + 1)

                
        return ans