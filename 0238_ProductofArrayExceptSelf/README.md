res[i] = (nums[0] * nums[1] * ... * nums[i-1]) * (nums[i+1] * ... * num[n-1])  

Space O(n) solution:  
use 2 lists to store cumulative product from left and from right  

Space O(1) (no extra space) solution:  
use 1 list to store cumulative product from left to right  
when calculate from right to left, we do not need to store all the list, just remember the previous number.   
