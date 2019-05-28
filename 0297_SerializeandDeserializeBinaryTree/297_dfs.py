# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # dfs
        res = ''
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                res += 'null'
            else:
                res += str(node.val)
                stack.append(node.right)
                stack.append(node.left)
            res += ','

        return res[:-1]
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        
        def helper(l):
            if l[0] == 'null':
                l.pop(0)
                return None

            root = TreeNode(int(l[0]))
            l.pop(0)
            root.left = helper(l)
            root.right = helper(l)
            return root
            
        return helper(l)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))