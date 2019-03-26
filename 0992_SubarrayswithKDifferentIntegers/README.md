Solution 1:
Count subarrays with at most K, at least 1 distinct numbers.

Then, subarrays with exact K numbers = atMost(K) - atMost(K-1)

Solution 2:
Use two sliding windows, small one with K - 1 numbers, large one with K numbers.

These two windows have same right boundary and different left boundaries. 
res += small_left - small_right

