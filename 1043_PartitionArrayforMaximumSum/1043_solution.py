class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [-float("Inf") for _ in range(N)]
        currMax = -float("Inf")
        for i in range(K):
            currMax = max(currMax, A[i])
            dp[i] = (i + 1) * currMax
        
        for i in range(K, N):
            currMax = -float("Inf")
            for k in range(K):
                currMax = max(currMax, A[i-k])
                dp[i] = max(
                    dp[i],
                    dp[i - k - 1] + (k + 1) * currMax
                )
            
        return dp[-1]
        