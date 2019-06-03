# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        left_ans = self.findLeaves(root.left)
        right_ans = self.findLeaves(root.right)
        
        res = []
        i = 0
        while i < len(left_ans) and i < len(right_ans):
            res.append(left_ans[i] + right_ans[i])
            i += 1
            
        if i == len(left_ans):
            res += right_ans[i:]
        else:
            res += left_ans[i:]
        
        res.append([root.val])
        return res