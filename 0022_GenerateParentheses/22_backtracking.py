class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(left, right, prev):
            if left == 0 and right == 0:
                res.append(prev)
                return
            
            if left == right:
                helper(left - 1, right, prev + '(')
                
            elif left < right:
                if left > 0:
                    helper(left - 1, right, prev + '(')
                helper(left, right - 1, prev + ')')
                
        helper(n, n, "")
        return res
                
                