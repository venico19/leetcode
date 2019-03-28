class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 2:
            return 0
        
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        
        res = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                res += max(left_max - height[left], 0)
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += max(right_max - height[right], 0)
                right -= 1
                
        return res
