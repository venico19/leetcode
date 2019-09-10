class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l_remove, r_remove = self.countRemove(s)
        res = []
        
        def backtracking(s, l_remove, r_remove, start):
            if l_remove == r_remove == 0 and self.isValid(s):
                res.append(s)
                return 
            i = start
            while i < len(s):
                if s[i] == ')' and r_remove > 0:
                    backtracking(s[:i]+s[i+1:], l_remove, r_remove - 1, i)
                elif s[i] == '(' and r_remove == 0 and l_remove > 0:
                    backtracking(s[:i]+s[i+1:], l_remove - 1, r_remove, i)
                # avoid duplicates
                while i < len(s) - 1 and s[i+1] == s[i]:
                    i += 1
                i += 1
                
        backtracking(s, l_remove, r_remove, 0)
        return res
                    
        
    def countRemove(self, s):
        left_count, right_count = 0, 0
        left_remove, right_remove = 0, 0
        for char in s:
            if char == '(':
                left_count += 1
            elif char == ')':
                right_count += 1
            
            if right_count > left_count:
                right_remove += 1
                right_count -= 1
                
        left_remove = left_count - right_count
        return left_remove, right_remove
    
    def isValid(self, s):
        left = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left == 0:
                    return False
                left -= 1
        return left == 0