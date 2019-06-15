class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        for i, num in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
            