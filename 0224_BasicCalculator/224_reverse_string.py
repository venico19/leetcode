class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(stack):
            res = 0
            sign = 1
            while stack:
                item = stack.pop()
                if item == ')':
                    break
                elif item == '-':
                    sign = -1
                elif item == '+':
                    sign = 1
                else:
                    res += sign * item
                
            return res
        
        stack = []
        temp = ''
        for char in s[::-1]:
            if char in ' +-()':
                if temp:
                    stack.append(int(temp[::-1]))
                    temp = ''
                if char in '+-)':
                    stack.append(char)
                    continue
                elif char == '(':
                    value = helper(stack)
                    stack.append(value)
            else:
                temp += char
                
        if temp:
            stack.append(int(temp[::-1]))
            
        return helper(stack)