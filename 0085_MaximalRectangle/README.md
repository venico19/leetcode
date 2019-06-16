**Solution 1**: dp  
dp[i][j]: 第i行以j结尾的最长width  
对每一个大于零的width，逐行向上看   
```
for k in range(i, -1, -1):
    width = min(width, dp[k][j])
    area = width * (i-k+1)
    max_area = max(max_area, area)
```
Time: O(N^2 * M)  (matrix dimension: m * n)  
Space: O(N * M)  

**Solution 2**: dp + stack   
dp的部分和solution 1类似，把solution 1里每一列dp看成一个histogram，这道题其实就是在求histogram下的最大面积（84题）。   
可以一列一列地处理dp，所以实际上不需要m * n的空间，只需要一个长度为m的list就够了。   
Time: O(N * M)  
Space: O(M)  

**Solution 3**: dp  
逐行更新，每个位置向上的最高height，以及这个height的左右限制(left right左闭右开)  
大致的思想是，如果height和上一行是连续的，那么left, right受限于上一行的left, right。同时要检查本行是否有0，来更新本行的curr_left, curr_right.   
当在一行里遇到0的时候，重置left, right。因为height接不上了……    
太难描述了看code吧……   
这个方法我自己想不出来orz……   
