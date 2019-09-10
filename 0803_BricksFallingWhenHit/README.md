暴力dfs模拟是会超时的……   

**Solution 1**: DFS, adding hit block in reversed order  
先把hits里的所有砖块都打掉，value - 1，原本是1的地方变成0，原本是0的地方变成了-1   
做一次dfs，把和ceiling相连的砖块都标记成2  
in a revered order, adding hit block back  
加回来的时候需要判断一下这个砖块是否和目前为2的砖块相连接，如果相连接且为1的话，从这个砖块开始做dfs，把相连的砖块都标记成2，并且在dfs中返回个数  
最后往res里加的时候记得减一（自己）  