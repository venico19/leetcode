class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        
        start = 0
        while start < n and nums[start] == 0:
            start += 1
        
        for i in range(start, n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - 1 - j
                
        return res