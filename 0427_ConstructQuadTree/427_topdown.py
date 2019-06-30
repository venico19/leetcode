"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        
        def isLeaf(r0, r1, c0, c1):
            for i in range(r0, r1):
                for j in range(c0, c1):
                    if grid[i][j] != grid[r0][c0]:
                        return False
            return True        

        
        def helper(r0, r1, c0, c1):
            if isLeaf(r0, r1, c0, c1):
                return Node(grid[r0][c0], True, None, None, None, None)
            else:
                tl = helper(r0, (r0+r1)//2, c0, (c0+c1)//2)
                tr = helper(r0, (r0+r1)//2, (c0+c1)//2, c1)
                bl = helper((r0+r1)//2, r1, c0, (c0+c1)//2)
                br = helper((r0+r1)//2, r1, (c0+c1)//2, c1)
                return Node('*', False, tl, tr, bl, br)
            
  
        return helper(0, N, 0, N)