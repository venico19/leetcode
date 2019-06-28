class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                value = stack.pop()
                if value // num < 0 and value % num != 0:
                    stack.append(value // num + 1)
                else:
                    stack.append(value // num)
                    
        stack = []
        num = 0
        op = '+'
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/)':
                update(op, num)
                if char == ')':
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    update(op, num)
                op, num = char, 0
            elif char == '(':
                stack.append(op)
                op, num = '+', 0
        update(op, num)
        
        return sum(stack)