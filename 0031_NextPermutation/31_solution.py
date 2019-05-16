class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        # starting from tail, move left, find the first decrease i
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        
        # swap nums[i] with the rightmost number A[j] where A[j] > A[i]
        if i > -1:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse nums[i+1:]
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        
            
        
