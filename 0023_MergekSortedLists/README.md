**Solution 1: heap**  
Time: O(nlogk)  
python3 直接往heap里push(node.val, node)会出问题，因为无法比较node。这样的写法在python2里是可以的。   
为了避免这个错，python3往heap里push(node.val, k, node), where k is linked list index. 这样比较tuple里的第二个元素就能比出大小，就不用比较node了。   

**Solution 2: divide and conquer (recusive)**  
similar to merge sort  
base case: merge 2 lists  

**Solution 3: iterative**  
similar to merge sort  
base case: merge 2 lists  