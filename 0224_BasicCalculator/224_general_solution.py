class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-':
                update(op, num)
                op = char
                num = 0
            elif char == '(':
                stack.append(op)
                op = '+'
            elif char == ')':
                update(op, num)
                num = 0
                while stack and isinstance(stack[-1], int):
                    num += stack.pop()
                op = stack.pop()
                update(op, num)
                op = char
                num = 0
        update(op, num)        
        
        return sum(stack)
        