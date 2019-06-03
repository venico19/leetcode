# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        # leaf has depth 0
        # depth increases from leaf to root

        def dfs(node):
            if not node:
                return -1
            depth = max(dfs(node.left), dfs(node.right)) + 1
            while len(res) < depth + 1:
                res.append([])
            res[depth].append(node.val)
            return depth
            
        dfs(root)
        return res
        
        