class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        res = 0
        visited = [False for _ in range(N)]
        for i in range(N):
            if visited[i]:
                continue
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                res += 1
                for nei in graph[node]:
                    if not visited[nei]:
                        stack.append(nei)
                        visited[nei] = True
            res -= 1
            
        return res
                