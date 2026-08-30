class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1

        return ans

        '''
        Performing n & (n - 1) removes the rightmost 1 bit from n
        while n:
            n &= n - 1
            ans += 1
        '''