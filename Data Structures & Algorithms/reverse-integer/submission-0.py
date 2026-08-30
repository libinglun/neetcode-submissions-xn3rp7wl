class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        if x == 0:
            return 0

        res = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x > 0:
            digit = x % 10
            x //= 10

            # Check if res exceeds the range
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit
        
        return res * sign