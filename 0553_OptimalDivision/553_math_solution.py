class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            res = str(nums[0]) + '/(' + str(nums[1])
            for num in nums[2:]:
                res += '/'
                res += str(num)
            res += ')'
            return res
