class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c != '+' and c != '*' and c != '-' and c != '/':
                stack.append(int(c))
            elif c == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            elif c == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            elif c == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            elif c == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
        return stack.pop()
        