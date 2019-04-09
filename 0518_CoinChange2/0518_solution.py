class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for c in coins:
            i = c
            while i <= amount:
                dp[i] += dp[i - c]
                i += 1

        return dp[amount]
        
