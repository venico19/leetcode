**Solution 1**  
Use two list to store max height from left and from right  
Water can be trapped on this bar[i] is (min(left_max[i], right_max[i]) - height[i])  
Space: O(n);  Time: O(n)    

**Solution 2**
The idea is similar to solution 1, but use two pointers to maintain left_max and right_max, avoid extra space.   
指针left从左边开始，指针right从右边开始，当height[left] <= height[right]时，right_max在此处必定大于left_max，（因为此处的right_max大于此处右边的所有height）。min(left_max[i], right_max[i]) = left_max[i]。  
当height[left] > height[right]时，类似地，min(left_max[i], right_max[i]) = right_max[i]  
Space: O(1); Time: O(n)  
