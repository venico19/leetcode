class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for [a, b] in prerequisites:
            graph[a].append(b)
        visited = [0 for _ in range(numCourses)]
        
        # visited:
        # 0: not visited
        # 1: good
        # -1: bad (in a circle)
        
        def dfs(a):
            if visited[a] == 1:
                return True
            if visited[a] == -1:
                return False
            
            visited[a] = -1
            for b in graph[a]:
                if not dfs(b):
                    return False
                
            visited[a] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True