class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parents = {}
        weights = {}
        
        def add(a):
            if a not in parents:
                parents[a] = a
                weights[a] = 1.0
                
        def find(a):
            if parents[a] == a:
                return a
            else:
                p = find(parents[a])
                weights[a] *= weights[parents[a]]
                parents[a] = p
                return p
            
        def union(a, b, val):
            add(a)
            add(b)
            p_a = find(a)
            p_b = find(b)
            if p_a != p_b:
                parents[p_a] = p_b
                weights[p_a] = val * weights[b] / weights[a]
                
        for i in range(len(equations)):
            a, b = equations[i]
            union(a, b, values[i])
            
        res = []
        for a, b in queries:
            if a not in parents or b not in parents:
                res.append(-1.0)
            else:
                if find(a) != find(b):
                    res.append(-1.0)
                else:
                    res.append(weights[a] / weights[b])
                    
        return res