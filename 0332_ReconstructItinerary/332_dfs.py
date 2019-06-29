class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        graph = collections.defaultdict(list)
        for [f, t] in tickets:
            bisect.insort(graph[f], t)
        
        def dfs(path, visited):
            if len(path) == N + 1:
                return path
            start = path[-1]
            if start not in graph:
                return []
            for i in range(len(graph[start])):
                if i in visited[start]:
                    continue
                # fly to graph[start][i]
                visited[start].add(i)
                ans = dfs(path + [graph[start][i]], visited)
                if ans != []:
                    return ans
                visited[start].remove(i)
                
            return []

        return dfs(['JFK'], collections.defaultdict(set))
        