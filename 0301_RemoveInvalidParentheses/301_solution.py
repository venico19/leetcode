class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l_remove, r_remove = 0, 0
        l_count, r_count = 0, 0
        for char in s:
            if char == '(':
                l_count += 1
            if char == ')':
                r_count += 1
            if r_count > l_count:
                r_remove += 1
                r_count -= 1
        l_remove = l_count - r_count
        
        def dfs(s, l_remove, r_remove, start):
            if l_remove == 0 and r_remove == 0 and self.isValid(s):
                res.append(s)
                return
            
            n = len(s)
            
            i = start
            while i < n:
                if s[i] == ')' and r_remove > 0:
                    dfs(s[:i]+s[i+1:], l_remove, r_remove - 1, i)
                if s[i] == '(' and r_remove == 0:
                    dfs(s[:i]+s[i+1:], l_remove - 1, r_remove, i)
                while i < n - 1 and s[i+1] == s[i]:
                    i += 1
                i += 1

        res = []
        dfs(s, l_remove, r_remove, 0)
        return res
        
    def isValid(self, s):
        stack = []
        for char in s:
            if char not in '()':
                continue
            if char == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            if char == '(':
                stack.append(char)
        return len(stack) == 0
        
