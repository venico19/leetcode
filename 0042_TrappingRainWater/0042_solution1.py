class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n == 0:
            return 0
        
        maxFromLeft, maxFromRight = [0 for _ in range(n)], [0 for _ in range(n)]
        
        maxFromLeft[0] = height[0]
        for i in range(1, n):
            maxFromLeft[i] = max(height[i], maxFromLeft[i-1])
            
        maxFromRight[n - 1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxFromRight[i] = max(height[i], maxFromRight[i+1])
            
        res = 0
        for i in range(n):
            res += max(min(maxFromLeft[i], maxFromRight[i]) - height[i], 0)
            
        return res
        
