# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root in [p, q]:
            return root
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)
        
        if left_res and right_res:
            return root
        elif left_res and not right_res:
            return left_res
        elif not left_res and right_res:
            return right_res
        else:
            return None