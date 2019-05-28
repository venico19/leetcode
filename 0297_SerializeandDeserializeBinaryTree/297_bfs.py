# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if not node:
                res += 'null'
            else:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            res += ','
        
        return res[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        datalist = data.split(',')
        n = len(datalist)
        
        if datalist[0] == 'null':
            return None
        
        root = TreeNode(int(datalist[0]))

        queue = collections.deque()
        queue.append(root)
        
        i = 1
        
        while i < n:
            node = queue.popleft()
            if datalist[i] != 'null':
                left = TreeNode(int(datalist[i]))
                node.left = left
                queue.append(left)
            i += 1
            if i == n:
                break
            if datalist[i] != 'null':
                right = TreeNode(int(datalist[i]))
                node.right = right
                queue.append(right)
            i += 1
            
        return root
            
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))