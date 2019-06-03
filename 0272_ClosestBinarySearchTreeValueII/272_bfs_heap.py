# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # BFS
        # use a max heap to keep smallest k res
        queue = collections.deque([root])
        heap = []
        
        while queue:
            node = queue.popleft()
            if not node:
                continue
            heapq.heappush(heap, (-abs(node.val - target), node.val, node))
            if len(heap) > k:
                _, _, pop_node = heapq.heappop(heap)
                if pop_node == node:
                    if node.val < target:
                        queue.append(node.right)
                    elif node.val > target:
                        queue.append(node.left)
                    continue

            queue.append(node.left)
            queue.append(node.right)
                
        res = []
        for _, val, _ in heap:
            res.append(val)
            
        return res