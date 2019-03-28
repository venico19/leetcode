**Solution 1**  
Use two list to store max height from left and from right  
Water can be trapped on this bar[i] is (min(left_max[i], right_max[i]) - height[i])  
Space: O(n);  Time: O(n)    

**Solution 2**  
The idea is similar to solution 1, but use two pointers to maintain left_max and right_max, avoid extra space.   
指针left从左边开始，指针right从右边开始，当height[left] <= height[right]时，right_max在此处必定大于left_max，（因为此处的right_max大于此处右边的所有height）。min(left_max[i], right_max[i]) = left_max[i]。  
当height[left] > height[right]时，类似地，min(left_max[i], right_max[i]) = right_max[i]  
Space: O(1); Time: O(n)  

**Solution 3**   
Stack
用stack记录height，保持stack里面的height永远是递减的，当新的一个height大于stack里最后一个height时，说明stack[-1]是一个被它两边挡住的valley，这个valley里的水量 = distance * (min(height, stack[-1]\_height) - valley_height)。  
需要注意的是distance的算法比较tricky, distance = i - stack[-1]\_index -1。经常犯的错是把distance写成valley_index - stack[-1]\_index。为什么呢，因为这个valley是从stack[-1].index的右边一直延伸到height左边的。想不明白的话看这个例子：[2, 1, 0, 1, 2]  
Space: O(n); Time: O(n)  
