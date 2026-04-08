class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        maxl = 0
        maxr = 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                print("maxl: ", maxl)
                res += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                res += maxr - height[r]
                r -= 1

            print(res)
        
        return res

            

