from fractions import Fraction
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        res = 0
        for i in range(n - 1):
            A = points[i]
            ans = 0
            duplicates = 1
            slope_counter = {}
            for j in range(i + 1, n):
                B = points[j]
                if A == B:
                    duplicates += 1
                    continue
                else:
                    s = self.slope(A, B)
                    slope_counter[s] = slope_counter.get(s, 0) + 1
                    ans = max(ans, slope_counter[s])
            ans += duplicates
            res = max(res, ans)
            
        return res
        
    def slope(self, A, B):
        if A[0] == B[0]:
            return float("Inf")
        return Fraction((B[1] - A[1]), (B[0] - A[0]))
    
    