class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
            
        cumSum = 0
        res = 0
        for num in nums:
            cumSum += num
            res += freq.get(cumSum - k, 0)
            freq[cumSum] = freq.get(cumSum, 0) + 1
            
        return res

            
            