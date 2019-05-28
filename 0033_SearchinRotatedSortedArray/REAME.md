binary search   
A[left:mid+1] 和 A[mid:right] 一定至少有一个是sorted   
先用A[left] <= A[mid]来判断左边半段是不是sorted，如果是且target在这个范围内，继续搜索A[left:mid；如果target不在这个范围里，搜索右半边。  
如果不满足A[left] <= A[mid]，那么右半边一定是sorted。类似处理。    