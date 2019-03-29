问题分解成几个部分：  
1. 检查一个string是否valid？ 
1.1. 可以用stack  
1.2. 对任意一个substring[0:i], count of '(' >= count of ')'; 对整个string，count of '(' == count of ')'  
2. 这个string需要去掉多少'(', 多少')'，才能valid？做法类似1.2   
3. 用dfs，先去掉')'，再去掉'('，尝试各种排列组合。  
3.1. 当有连续'((('或者')))'时，只尝试去掉第一个括号，避免重复。   
