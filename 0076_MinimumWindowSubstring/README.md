Solution 1:  
sliding window   
用一个set记录哪些字母已经满足要求了  

Solution 2在solution 1的基础上预先filter了s，只保留了在t里出现过的字母。用filtered_s记录了(index, char)的组合。   
要注意，loop filtered_s的时候搞清楚，index到底是s的index还是filtered_s的index。   
当filtered_s远小于s的时候solution 2会快一点儿。   