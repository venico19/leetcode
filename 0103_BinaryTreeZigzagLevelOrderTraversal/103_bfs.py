# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        left_to_right = True
        currLevel = []
        nextLevel = [root]
        while currLevel or nextLevel:
            if not currLevel:
                currLevel = nextLevel[:]
                nextLevel = []
                values = []
                for node in currLevel:
                    values.append(node.val)
                if left_to_right:
                    res.append(values[:])
                else:
                    res.append(values[::-1])
                left_to_right = not left_to_right
            
            node = currLevel.pop(0)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
                
        return res
