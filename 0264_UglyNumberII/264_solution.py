import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        candidates = [1]
        currUgly = 1
        
        for _ in range(n - 1):
            # generate next ugly number
            for prime in [2,3,5]:
                heapq.heappush(candidates, currUgly * prime)
            while candidates[0] <= currUgly:
                heapq.heappop(candidates)
            currUgly = candidates[0]
            
        return currUgly
        
