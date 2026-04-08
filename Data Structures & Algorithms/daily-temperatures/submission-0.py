class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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

        