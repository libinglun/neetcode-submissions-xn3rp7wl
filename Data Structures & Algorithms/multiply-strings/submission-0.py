class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i, s1 in enumerate(num1):
            for j, s2 in enumerate(num2):
                mul = int(s1) * int(s2)
                total = res[i + j] + mul
                res[i + j] = total % 10
                res[i + j + 1] += total // 10

        if res[-1] == 0:
            res.pop()

        return "".join(map(str, res[::-1]))
