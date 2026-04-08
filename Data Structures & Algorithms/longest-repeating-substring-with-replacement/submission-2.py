class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {s[0]: 1}
        l = 0
        r = 0
        ans = r - l
        while l <= r and r < len(s):
            print(freq, l, r)
            if sum(freq.values()) - max(freq.values()) <= k:
                ans = max(ans, r - l + 1)
                r += 1
                if r == len(s):
                    break
                if s[r] not in freq:
                    freq[s[r]] = 0
                freq[s[r]] += 1
            else:
                freq[s[l]] -= 1
                l += 1
                
        return ans