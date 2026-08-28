class Solution:
    def isHappy(self, n: int) -> bool:

        def replace(n):
            res = 0
            while n > 0:
                digit = n % 10
                n //= 10
                res += digit**2

            return res

        number = set()
        while n != 1:
            if n in number:
                return False
            number.add(n)
            n = replace(n)

        return True


        