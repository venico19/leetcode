class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def backtracking(i):
            if i == n:
                res.append(nums[:])
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtracking(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                
        backtracking(0)
        return res