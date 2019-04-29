Solution1和Solution2都是dp。    
Solution1：dp[i][diff]是以A[i]结尾的公差为diff的sequence个数，包括长度为2的sequence。所以必须检查，当diff in dp[j] (j<i)时，才能保证dp[j][diff]的sequence加上A[i]构成了个数>=3的sequence，这时把dp[j][diff]的数字加入res。   
Solution2更直观。dp[i][diff]是以A[i]结尾的公差为diff的sequence个数，sequence必须>=3。所以要检查是否有至少3个数组成了sequence，至少有3个数的时候才更新dp[i][diff]。最后的res就是把dp里的所有数字加起来。   

