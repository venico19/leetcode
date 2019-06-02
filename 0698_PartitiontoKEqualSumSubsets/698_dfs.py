class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s%k != 0:
            return False
        target = s//k
        if max(nums) > target:
            return False

        subsets = [target for _ in range(k)]
        nums = sorted(nums)[::-1]
        n = len(nums)
        
        def search(i, subsets):
            if i == n:
                return sum(subsets) == 0
            
            num = nums[i]
            
            subsets.sort()
            for j in range(k):
                if j < k - 1 and subsets[j] == subsets[j+1]:
                    continue
                if subsets[j] - num >= 0:
                    new_subsets = subsets[:]
                    new_subsets[j] -= num
                    if search(i + 1, new_subsets):
                        return True
                    
            return False
        
        return search(0, subsets)
        
            