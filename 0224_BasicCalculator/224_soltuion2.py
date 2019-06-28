class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        temp = 0
        for char in s:
            if char.isdigit():
                temp = temp * 10 + int(char)
            elif char in ' +-()':
                res += sign * temp
                temp = 0
                
                if char == '+':
                    sign = 1
                elif char == '-':
                    sign = -1
                elif char == '(':
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif char == ')':
                    res *= stack.pop()
                    res += stack.pop()

        res += sign * temp
        return res
