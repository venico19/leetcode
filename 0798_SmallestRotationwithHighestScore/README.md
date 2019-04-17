大致思路：   
对每一个数字，找到能得分的good k range，在同一个list里记录这个range的开头结尾   
然后用cum sum统计k取每个value时能得多少分。   


Example: [2, 3, 1, 4, 0]   
number worths point when number <= index   
A[0] = 2   
good index range is [num, n-1], here is [2, 4]    
good k range is [(i - (n-1))%n, (i-num)%n], here is [1,3]   
good k range is [(i - (n-1))%n, (i-num+1)%n), here is [1,4)   
为什么要用左闭右开区间？因为我们想找到从哪个数开始，k is good (which is 1 here)。也需要找到从哪个数开始，k is not good (which is 4 here)    
有了这样的左闭右开区间后，不需要对区间内的每一个k += 1。用一个good list, good[left] += 1, good[right] -= 1. 对good做从左到右的cum sum，就可以得到k得分的range。   
for example，A[0] = 2, left = 1, right = 4, good = [0, 1, 0, 0, -1].   
cum sum of good is: [0, 1, 1, 1, 0], which is good range for k.   

if we loop all good k and do good[k] += 1, total time complexity will be O(n^2)  
if we only record good k range left and right points, time complextity is O(n)  

还有一点需要处理的：如果good k range不连续怎么办？   
for example, A[2] = 1,  good k range: [3, 4, 0, 1], left = 3, right = 2, left > right   
这个range可以拆成[3, 5), [0, 2)   
对good list，除了上面提到的good[3] += 1, good[2] -= 1这两个操作，还需要加上good[5] -= 1, good[0] += 1.   
实际操作中不用管good[5], 5 is not a valid value for k.   


