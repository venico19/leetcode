class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        upper = min(A[0][0], A[R-1][C-1])
        
        L = set()
        for i in range(R):
            for j in range(C):
                if A[i][j] <= upper:
                    L.add(A[i][j])
        L = sorted(list(L), reverse = True)

        left, right = 0, len(L) - 1
        while left < right:
            mid = (left + right) // 2
            if self.isValid(A, L[mid]):
                right = mid
            else:
                left = mid + 1
        return L[left]
            
        
    def isValid(self, A, score):
        R, C = len(A), len(A[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        visited.add((0, 0))
        
        def backtracking(i, j):
            if i == R - 1 and j == C - 1:
                return True
            for x, y in directions:
                if i+x < 0 or i+x >= R or j+y < 0 or j+y >= C:
                    continue
                if (i+x, j+y) in visited or A[i+x][j+y] < score:
                    continue
                visited.add((i+x, j+y))
                if backtracking(i+x, j+y):
                    return True
            return False

        return backtracking(0, 0)                