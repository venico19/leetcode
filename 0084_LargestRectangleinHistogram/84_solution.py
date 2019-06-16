class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        