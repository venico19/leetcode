class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.bit = [0 for _ in range(self.N + 1)]
        for i, num in enumerate(nums):
            self._update_bit(i+1, num)
    
    def _update_bit(self, i, num):
        while i <= self.N:
            self.bit[i] += num
            i += self._lowbit(i)
            
    def _getsum_bit(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self._lowbit(i)
        return res
        
    def _lowbit(self, x):
        return x & (-x)

    def update(self, i: int, val: int) -> None:
        delta = val - self.sumRange(i, i)
        self._update_bit(i + 1, delta)

    def sumRange(self, i: int, j: int) -> int:
        if self.N == 0:
            return 0
        return self._getsum_bit(j+1) - self._getsum_bit(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)