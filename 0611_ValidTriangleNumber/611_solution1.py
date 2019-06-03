import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                limit = nums[i] + nums[j]
                k = bisect.bisect_left(nums, limit)
                if k - 1 > j:
                    res += k - 1 - j
                    
        return res
                