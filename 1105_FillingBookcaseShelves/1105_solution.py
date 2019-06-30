class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N = len(books)
        dp = [float("Inf") for _ in range(N + 1)]
        dp[0] = 0
        
        for i in range(1, N + 1):
            j = i - 1
            w, h = books[i-1]
            while w <= shelf_width and j >= 0:
                dp[i] = min(
                    dp[i], 
                    dp[j] + h
                )
                if j == 0:
                    break
                w += books[j-1][0]
                h = max(h, books[j-1][1])
                j -= 1
                
        return dp[-1]
                
            