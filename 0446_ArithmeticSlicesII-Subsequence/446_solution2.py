class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        
        lookup = {}
        for i, num in enumerate(A):
            if num not in lookup:
                lookup[num] = []
            lookup[num].append(i)
        
        # dp[i][diff]: sequence with >=3 elements ending with A[i]
        dp = [{} for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                X = A[j] - diff
                # X, A[j], A[i] is a sequence
                if X in lookup:
                    for index in lookup[X]:
                        if index >= j:
                            break
                        dp[i][diff] = dp[i].get(diff, 0) + 1
                # adding sequence with diff ending with A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]
                                
        res = 0
        for i in range(n):
            for k in dp[i]:
                res += dp[i][k]
                
        return res