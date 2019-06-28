class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        temp = 0
        sign = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                temp = temp * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(temp)
                elif sign == '-':
                    stack.append(-temp)
                elif sign == '*':
                    stack.append(stack.pop() * temp)
                else:
                    value = stack.pop()
                    if value // temp < 0 and value % temp != 0:
                        stack.append(value//temp + 1)
                    else:
                        stack.append(value//temp)
                sign = char
                temp = 0
      
        return sum(stack)