class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}
        for i, value in enumerate(values):
            numerator, denominator = equations[i]
            if numerator not in g:
                g[numerator] = {}
                g[numerator][numerator] = 1.0
            if denominator not in g:
                g[denominator] = {}
                g[denominator][denominator] = 1.0
            g[numerator][denominator] = value
            g[denominator][numerator] = 1.0/value
        
        res = []
        for a, b in queries:
            res.append(self.calculate(a, b, g))
            
        return res
            
    def calculate(self, a, b, g):
        if a not in g or b not in g:
            return -1.0
        
        def dfs(a, b, prev, visited):
            if b in g[a]:
                return prev * g[a][b]
            for nei in g[a]:
                if nei in visited:
                    continue
                else:
                    visited.add(nei)
                    ans = dfs(nei, b, prev * g[a][nei], visited)
                    if ans != -1.0:
                        return ans
                    else:
                        visited.remove(nei)
            return -1.0
                    
        return dfs(a, b, 1.0, set([a]))