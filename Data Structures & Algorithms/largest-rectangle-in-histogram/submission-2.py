class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(heights):
            index = i
            if not len(stack):
                stack.append((index, h))
            else:
                while len(stack) and h < stack[-1][1]:
                    index, height = stack.pop()
                    ans = max(ans, height * (i - index))
                stack.append((index, h))
                print(stack)

        for i, h in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans