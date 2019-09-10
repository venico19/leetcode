# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.backtracking(root, {0:1}, 0, 0, sum)
        
    def backtracking(self, node, preSum, cumSum, res, target):
        if not node:
            return res
        cumSum += node.val
        res += preSum.get(cumSum - target, 0)
        preSum[cumSum] = preSum.get(cumSum, 0) + 1
        res = self.backtracking(node.left, preSum, cumSum, res, target)
        res = self.backtracking(node.right, preSum, cumSum, res, target)
        preSum[cumSum] -= 1
        return res