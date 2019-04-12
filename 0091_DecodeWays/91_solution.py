class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        
        # dp[i]: decode ways for s[:i]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            prev2Char = s[i-2:i]
            if prev2Char >= '10' and prev2Char <= '26':
                dp[i] += dp[i-2]
                
            currChar = s[i - 1]
            if currChar != '0':
                dp[i] += dp[i-1]

        return dp[n]