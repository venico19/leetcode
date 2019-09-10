# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        
        stack = [root]
        while stack[-1].left:
            stack.append(stack[-1].left)
            
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                while stack[-1].left:
                    stack.append(stack[-1].left)
                
        return res
        