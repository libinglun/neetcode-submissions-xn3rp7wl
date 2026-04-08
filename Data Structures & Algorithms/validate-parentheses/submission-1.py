class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if c == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if c == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                continue

        return len(stack) == 0
        