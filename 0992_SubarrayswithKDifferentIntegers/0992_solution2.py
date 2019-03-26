class Window:
    def __init__(self):
        self.counter = {}
        self.count = 0
        
    def add(self, num):
        if not num in self.counter:
            self.count += 1
        self.counter[num] = self.counter.get(num, 0) + 1
    
    def remove(self, num):
        self.counter[num] -= 1
        if self.counter[num] == 0:
            del self.counter[num]
            self.count -= 1

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        wLarge, wSmall = Window(), Window()
        leftL, leftS = 0, 0
        res = 0
        
        for num in A:
            wLarge.add(num)
            wSmall.add(num)
            
            while wLarge.count > K:
                wLarge.remove(A[leftL])
                leftL += 1
                
            while wSmall.count >= K:
                wSmall.remove(A[leftS])
                leftS += 1
                
            res += leftS - leftL
            
        return res

