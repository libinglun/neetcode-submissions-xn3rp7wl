class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            sum_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            
            if sum_bit:
                res |= (1 << i)

        MAX_INT = 0x7FFFFFFF  # 2^31 - 1
        MASK = 0xFFFFFFFF
        
        return res if res <= MAX_INT else ~(res ^ MASK)