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
        n = len(grid)
        
        def helper(i, j, l):
            if l == 1:
                return Node(grid[i][j] == 1, True, None, None, None, None)
            else:
                tl = dfs(i, j, l // 2)
                tr = dfs(i, j + l //2, l // 2)
                bl = dfs(i + l // 2, j, l // 2)
                br = dfs(i + l // 2, j + l // 2, l // 2)
                if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                    return Node(grid[i][j] == 1, True, None, None, None, None)
                else:
                    return Node('*', False, tl, tr, bl, br)
    
        return helper(0, 0, n)