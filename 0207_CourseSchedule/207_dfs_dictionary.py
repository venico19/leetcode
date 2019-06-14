class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        for [a, b] in prerequisites:
            if a not in g:
                g[a] = []
            g[a].append(b)
            
        good = set()
        bad = set()
        
        def dfs(a, visited):
            if a not in g or a in good:
                good.add(a)
                return True
            if a in bad:
                return False
            
            visited.add(a)
            for b in g[a]:
                if b in visited:
                    bad.add(a)
                    return False
                if not dfs(b, visited):
                    bad.add(a)
                    return False
                
            good.add(a)
            return True
                         
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True
                