class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        
        n, k = len(costs), len(costs[0])
        
        if k == 1:
            return costs[0][0] if n == 1 else None
        
        # smallest and 2nd smallest (index, value)
        first, second = (-1, float("Inf")), (-1, float("Inf"))
        
        # initialize first and second
        for j in range(k):
            if costs[0][j] <= first[1]:
                second = first
                first = (j, costs[0][j])
            elif costs[0][j] < second[1]:
                second = (j, costs[0][j])

        for i in range(1, n):
            curr_first, curr_second = (-1, float("Inf")), (-1, float("Inf"))
            for j in range(k):
                if j != first[0]:
                    costs[i][j] += first[1]
                else:
                    costs[i][j] += second[1]
                    
                if costs[i][j] <= curr_first[1]:
                    curr_second = curr_first
                    curr_first = (j, costs[i][j])
                elif costs[i][j] < curr_second[1]:
                    curr_second = (j, costs[i][j])

            first, second = curr_first, curr_second

        return min(costs[-1])