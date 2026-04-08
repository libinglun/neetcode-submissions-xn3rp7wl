class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countt = {}
        for c in t:
            countt[c] = countt.get(c, 0) + 1

        minlen = len(s) + 1
        minstr = ""
        
        l = 0
        for r in range(len(s)):
            if s[r] in countt:
                countt[s[r]] -= 1
            while all(cnt <= 0 for cnt in countt.values()):
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    minstr = s[l:r+1]

                if s[l] not in countt:
                    l += 1
                else:
                    if countt[s[l]] < 0:
                        countt[s[l]] += 1
                        l += 1
                    else:
                        break
                

        print(l, r)
        print(sum(countt.values()))
        if sum(countt.values()) > 0:
            return ""
        else:
            return minstr
                



            

        
        