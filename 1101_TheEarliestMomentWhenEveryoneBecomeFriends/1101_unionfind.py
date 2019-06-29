class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort()
        parents = list(range(N))
        groups = [N]
        
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
            
        def union(i, j):
            p_i = find(i)
            p_j = find(j)
            if p_i != p_j:
                groups[0] -= 1
                if p_i > p_j:
                    parents[p_j] = p_i
                else:
                    parents[p_i] = p_j
                    
        for (timestamp, i, j) in logs:
            union(i, j)
            if groups[0] == 1:
                return timestamp
            
        return -1