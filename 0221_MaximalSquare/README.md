**Dynamic Programming**  
dp[i][j]: size of max square including grid[i][j]  
if matrix[i][j] == 1:  
    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1  
    res = max(res, dp[i][j] ** 2)  

Time: O(mn)   
Space: O(mn)   

Better solution:   
use a vector to store dp states, we do not need to store all previous states.   
Time: O(mn)  
Space: O(n)  
