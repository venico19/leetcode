class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        height = [0 for _ in range(n)]
        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        
        res = 0
        
        for i in range(m):
            curr_left, curr_right = 0, n
            
            # update height
            for j in range(n):            
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
                    
            # update left
            for j in range(n):
                if matrix[i][j] == '0':
                    left[j] = 0
                    curr_left = j + 1
                else:
                    left[j] = max(left[j], curr_left)
                    
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '0':
                    right[j] = n
                    curr_right = j
                else:
                    right[j] = min(right[j], curr_right)
                    
            # update area
            for j in range(n):
                res = max(res, height[j] * (right[j] - left[j]))
        
        return res