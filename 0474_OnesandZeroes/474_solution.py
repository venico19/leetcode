class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]: max number of string with i 0s and j 1s
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 0
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m - zeros, -1, -1):
                for j in range(n - ones, -1, -1):
                    if dp[i][j] >= 0:
                        dp[i+zeros][j+ones] = max(dp[i+zeros][j+ones], dp[i][j] + 1)

        return max(max(x) for x in dp)
