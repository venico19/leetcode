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
            elif char in '+-*/':
                update(op, num)
                num = 0
                op = char
        update(op, num)
                
        return sum(stack)
            