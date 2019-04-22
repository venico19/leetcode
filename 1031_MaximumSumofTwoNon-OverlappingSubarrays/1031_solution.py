class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """
        O(n) solution
        Lsum: sum of last L elements
        Msum: sum of last M elements
        Lmax: max sum of L contiguous elements before last M elements
        Mmax: max sum of M contiguous elements before last L elements
        """
        N = len(A)
        for i in range(1, N):
            A[i] += A[i - 1]
            
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        
        for i in range(L + M, N):
            Lsum = A[i] - A[i - L]
            Msum = A[i] - A[i - M]
            Lmax = max(Lmax, A[i - M] - A[i - M - L])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + Msum, Mmax + Lsum)
            
        return res
        