class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        heap = [(-A[0][0], 0, 0)]
        visited = [[0 for _ in range(C)] for _ in range(R)]
        visited[0][0] = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while heap:
            negScore, i, j = heapq.heappop(heap)
            if i == R - 1 and j == C - 1:
                return -negScore
            for x, y in directions:
                if i + x < 0 or i + x >= R or j + y < 0 or j + y >= C or visited[i+x][j+y] == 1:
                    continue
                visited[i+x][j+y] = 1
                heapq.heappush(heap, (max(negScore, -A[i+x][j+y]), i+x, j+y))