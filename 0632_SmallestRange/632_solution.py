class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        K = len(nums)
        heap = []
        heapmax = -float("Inf")
        
        for k in range(K):
            heapq.heappush(heap, (nums[k][0], k, 0))
            heapmax = max(heapmax, nums[k][0])
            
        res_left, res_right = heap[0][0], heapmax
        
        while len(heap) == K:
            _, k, i = heapq.heappop(heap)
            if i < len(nums[k]) - 1:
                heapq.heappush(heap, (nums[k][i+1], k, i+1))
                heapmax = max(heapmax, nums[k][i+1])
                if heapmax - heap[0][0] < res_right - res_left:
                    res_right, res_left = heapmax, heap[0][0]
        
        return res_left, res_right
        
            