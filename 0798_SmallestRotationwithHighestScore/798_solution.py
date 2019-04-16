class Solution:
    def bestRotation(self, A: List[int]) -> int:
        if not A:
            return 0
        
        n = len(A)
        good = [0 for _ in range(n)]
        
        for i, num in enumerate(A):
            if num == 0 or num >= n:
                continue
            
            # num worths point when k in [left_good_k, right_good_k)
            left_good_k = (i - n + 1) % n
            right_good_k = (i - num + 1) % n
            
            good[left_good_k] += 1
            good[right_good_k] -= 1
            if left_good_k > right_good_k:
                good[0] += 1

        best = 0
        ans = 0
        cur = 0
        for i, score in enumerate(good):
            cur += score
            if cur > best:
                best = cur
                ans = i
                
        return ans
