# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        preSum = collections.defaultdict(list)
        return self.backtracking(root, preSum, 0, [], [], sum)
        
    def backtracking(self, node, preSum, cumSum, path, res, target):
        if not node:
            return res
        
        cumSum += node.val
        path.append(node.val)
        
        # add all possible paths to result
        if cumSum - target in preSum:
            for pre in preSum[cumSum - target]:
                res.append(path[len(pre):])
        preSum[cumSum].append(path[:])
        
        res = self.backtracking(node.left, preSum, cumSum, path, res, target)
        res = self.backtracking(node.right, preSum, cumSum, path, res, target)
        
        # remove this node 
        path.pop()
        preSum[cumSum].pop()
        return res