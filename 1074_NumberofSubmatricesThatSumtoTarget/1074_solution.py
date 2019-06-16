class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j - 1]
        
        res = 0
        
        for i in range(n):
            for j in range(i, n):
                currSum = 0
                counter = {0: 1}
                for k in range(m):
                    currSum += matrix[k][j]
                    if i > 0:
                        currSum -= matrix[k][i - 1]
                    res += counter.get(currSum - target, 0)
                    counter[currSum] = counter.get(currSum, 0) + 1
                    
        return res