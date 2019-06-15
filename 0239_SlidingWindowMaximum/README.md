O(n) solution:  
Use a monotonic queue to store index in sliding window,   
for every i j in queue and i < j, nums[i] > nums[j]   
queue[0] is the largest number's index in the sliding window.   
pop from left when sliding window and the leftmost index is out of window   
