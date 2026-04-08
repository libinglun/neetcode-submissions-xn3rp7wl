class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                if token == '-':
                    result = operand1 - operand2
                if token == '*':
                    result = operand1 * operand2
                if token == '/':
                    result = int(operand1 / operand2)
                stack.append(result)

            print(stack)
        
        print(stack)
        return stack[-1]
        