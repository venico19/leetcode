class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = [[] for _ in range(n)]
        
        for i in range(n):
            for nei in graph[i]:
                rev_graph[nei].append(i)
        graph_map = {}
        for i in range(n):
            graph_map[i] = set(graph[i])
                
        good = set()
        queue = collections.deque()
        
        for i in range(n):
            if graph[i] == []:
                queue.append(i)
                
        while queue:
            i = queue.popleft()
            good.add(i)
            for j in rev_graph[i]:
                graph_map[j].remove(i)
                if len(graph_map[j]) == 0:
                    queue.append(j)
                    
        return sorted(list(good))