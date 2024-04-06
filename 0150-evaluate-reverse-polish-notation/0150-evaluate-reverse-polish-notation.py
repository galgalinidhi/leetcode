class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            # print(stack)
            if tokens[i].isnumeric():
                stack.append(int(tokens[i]))
            elif tokens[i][0] == '-' and tokens[i][1:].isnumeric():
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                op2= stack.pop()
                op1 = stack.pop()
                res = op1+op2
                stack.append(res)
            elif tokens[i] == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1-op2
                stack.append(res)
            elif tokens[i] == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1*op2
                stack.append(res)
            elif tokens[i] ==  '/':
                op2 = stack.pop()
                op1 = stack.pop()
                res = int(op1/op2)
                stack.append(res)
            else:
                continue
        return stack[-1]        