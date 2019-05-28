import random
class Solution:

    def __init__(self, w: List[int]):
        self.cdf = []
        s = sum(w)
        cumsum = 0
        for num in w:
            cumsum += num
            self.cdf.append(cumsum/s)
        self.size = len(self.cdf)

    def pickIndex(self) -> int:
        target = random.random()
        l, r = 0, self.size - 1
        
        while l < r:
            mid = (l + r) // 2
            if self.cdf[mid] == target:
                return mid
            elif self.cdf[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()