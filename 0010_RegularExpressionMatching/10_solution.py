class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}
        
        def dp(i, j):
            # if s[i:] and p[j:] match
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == n:
                ans = i == m
            else:
                if i == m:
                    firstMatch = False
                else:
                    firstMatch = p[j] in [s[i], '.']
                
                if j < n - 1 and p[j + 1] == '*':
                    ans = dp(i, j + 2) or (firstMatch and dp(i + 1, j))
                else:
                    ans = firstMatch and dp(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)