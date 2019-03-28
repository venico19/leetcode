class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 2:
            return 0
        
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                valley_index, valley_height = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1][0] - 1
                res += distance * (min(h, stack[-1][1]) - valley_height)
            stack.append((i, h))
            
        return res
        
