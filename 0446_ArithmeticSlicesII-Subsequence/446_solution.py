class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        
        # dp[i][diff]: number of arithmetic sequence with diff ending with A[i]
        # including artiehmetic sequece with only 2 elements
        dp = [{} for _ in range(n)]
        res = 0
        
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                # adding the sequence with only 2 elements
                dp[i][diff] = dp[i].get(diff, 0) + 1
                if diff in dp[j]:
                    res += dp[j][diff]
                    # dp[j][diff] + A[i] is number of sequence with >=3 elements
                    dp[i][diff] += dp[j][diff]
        
        return res