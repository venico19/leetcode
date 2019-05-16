class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        odd = [False for _ in range(n - 1)] + [True]
        even = [False for _ in range(n - 1)] + [True]
        
        def nextIndex(indexes):
            ans = [None for _ in range(n)]
            stack = []
            for i in indexes:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
        
        indexes = sorted(range(n), key = lambda i: A[i])
        nextOdd = nextIndex(indexes)
        indexes = sorted(range(n), key = lambda i: -A[i])
        nextEven = nextIndex(indexes)
        
        for i in range(n-2, -1, -1):
            if nextOdd[i]:
                odd[i] = even[nextOdd[i]]
            if nextEven[i]:
                even[i] = odd[nextEven[i]]
                
        return sum(odd)