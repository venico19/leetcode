class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        # from left to right
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        # from right to left
        cumProduct = 1
        for i in range(n-2, -1, -1):
            cumProduct *= nums[i+1]
            res[i] *= cumProduct
        return res
