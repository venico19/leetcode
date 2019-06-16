class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        # dp[i]: continous width on ith row
        dp = [0 for _ in range(m)]
        res = 0
        
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i] + 1
            
            res = max(res, self.maxAreaHistogram(dp))
            
        return res
  
    def maxAreaHistogram(self, heights):
        n = len(heights)
        
        res = 0
        stack = [[-1, 0]]
        for i, height in enumerate(heights):
            curr_i = i
            while height < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                res = max(res, prev_h * (i - prev_i))
                curr_i = prev_i
            stack.append([curr_i, height])
            
        while stack:
            i, h = stack.pop()
            res = max(res, h * (n - i))
            
        return res        
        