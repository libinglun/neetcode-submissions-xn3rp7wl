class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i

        return res
        '''
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((t, i))
            else:
                while len(stack) and t > stack[-1][0]:
                    _, index = stack.pop()
                    result[index] = i - index
                stack.append((t, i))
        
        return result
        '''

        