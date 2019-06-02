# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        l = self.parse(S)
        depth, val = l.pop(0)
        root = TreeNode(val)
        
        def dfs(node, depth, leftFlag):
            if not l or l[0][0] != depth + 1:
                return
            
            _, val = l.pop(0)
            nextNode = TreeNode(val)
            if leftFlag:
                node.left = nextNode
            else:
                node.right = nextNode 
                
            dfs(nextNode, depth + 1, True)
            dfs(nextNode, depth + 1, False)
            
        dfs(root, 0, True)
        dfs(root, 0, False)
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