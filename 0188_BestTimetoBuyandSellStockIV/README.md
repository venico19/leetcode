dp[i][j]: max profit with i transactions on day j  
local[j]: maxprofit, must sell on day j  必须在第j天有一次卖出  

```
profit = prices[j] - prices[j - 1]
local[j] = max(
    dp[i-1][j-1] + profit,
    dp[i-1][j-1],
    local[j-1] + profit
)
dp[i][j] = max(dp[i][j-1], local[j])
```

更新local[j]分三种情况：   
1) dp[i-1][j-1] + profit. dp[i-1][j-1]是发生过i-1次交易，在第j-1天的最大收益。在这个基础上再做一次交易：第j-1天买，第j天卖。  
2) dp[i-1][j-1]. 和1)类似，但第j天买，第j天卖（相当于什么都没做）  
3) local[j-1] + profit. 在local[j-1]的基础上，第j-1天买，第j天卖。因为local[j-1]一定有一次在j-1天发生的卖出。这种情况相当于cancel了j-1天的那次卖出，改为j天卖出。实际的交易次数并没有增加。   