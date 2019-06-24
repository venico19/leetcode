class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0 for _ in range(n)] 
        
        # 0: not visited
        # -1: visited
        # 1: bad
        # 2: good
        
        def dfs(i):
            if visited[i] == 2:
                return True
            if visited[i] == -1:
                visited[i] = 1
            if visited[i] == 1:
                return False
            
            visited[i] = -1
            for nei in graph[i]:
                if not dfs(nei):
                    visited[i] = 1
                    return False
                
            visited[i] = 2
            return True
        
        res = []
        for i in range(n):
            dfs(i)
            if visited[i] == 2:
                res.append(i)
                
        return res
            