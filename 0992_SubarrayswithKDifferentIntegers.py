class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysAtMostK(A, K) - self.subarraysAtMostK(A, K - 1)
        
    def subarraysAtMostK(self, A, K):
        counter = {}
        left = 0
        res = 0
        for right, num in enumerate(A):
            counter[num] = counter.get(num, 0) + 1
            while len(counter) > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    del counter[A[left]]
                left += 1
                    
            res += right + 1 - left
            
        return res