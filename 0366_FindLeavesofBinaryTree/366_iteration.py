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

        parent = {}
        
        stack = [root]
        leaves = []
        res = []
        
        def dropLeaf(leaf):
            if leaf in parent:
                p = parent[leaf]
                if p.left == leaf:
                    p.left = None
                elif p.right == leaf:
                    p.right = None
        
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            if not node.left and not node.right:
                leaves.append(node)
        
        while leaves:
            next_leaves = []
            leaves_val = []
            for l in leaves:
                leaves_val.append(l.val)
                dropLeaf(l)
                if l in parent:
                    p = parent[l]
                    if not p.left and not p.right:
                        next_leaves.append(p)
                    
            res.append(leaves_val)
            leaves = next_leaves

        return res
            
        
        