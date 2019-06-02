# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        l = self.parse(S)
        
        if not l:
            return None
        
        root = TreeNode(l[0][1])
        stack = [(0, root)]
        
        for (depth, val) in l[1:]:
            node = TreeNode(val)
            while depth < stack[-1][0] + 1:
                stack.pop()
            parentNode = stack[-1][1]
            if not parentNode.left:
                parentNode.left = node
            else:
                parentNode.right = node
                stack.pop()
            stack.append((depth, node))

        return root
        
    def parse(self, S):
        # parse the string to a [(depth, val)] list
        l = S.split('-')
        res = [(0, l[0])]
        
        depth = 1
        for item in l[1:]:
            if item != '':
                res.append((depth, int(item)))
                depth = 1
            elif item == '':
                depth += 1
                
        return res