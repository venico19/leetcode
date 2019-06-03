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
            return (1, 0)
        elif A[1] == B[1]:
            return (0, 1)
        else:
            numerator = B[1] - A[1]
            denominator = B[0] - A[0]
            gcd = self.findGcd(numerator, denominator)
            numerator //= gcd
            denominator //= gcd
            if numerator < 0:
                numerator *= -1
                denominator *= -1
            return (numerator, denominator)

    
    def findGcd(self, A, B):
        A, B = abs(A), abs(B)
        if B > A:
            A, B = B, A
            
        if A % B == 0:
            return B
        else:
            return self.findGcd(B, A%B)
    
    