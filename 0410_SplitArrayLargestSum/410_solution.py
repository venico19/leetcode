class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # binary search
        upper = sum(nums)
        lower = max(nums)
        
        while lower < upper:
            mid = (lower + upper) // 2
            if self.isPartitionValid(nums, m, mid):
                upper = mid
            else:
                lower = mid + 1
                
        return upper
        
    def isPartitionValid(self, nums, m, limit):
        # check if nums could be split to m parts with each part's sum <= limit
        count = 1
        total = 0
        for num in nums:
            if total + num <= limit:
                total += num
            else:
                total = num
                count += 1
                if count > m:
                    return False
        return True

