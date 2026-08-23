class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []

        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            elif v == '*':
                star.append(i)
            elif v == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack and star:
            if stack.pop() > star.pop():
                return False

        return not stack


        