class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lower = matrix[0][0]
        upper = matrix[-1][-1]
        
        while lower < upper:
            mid = (lower + upper) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lower = mid + 1
            else:
                upper = mid
                
        return lower