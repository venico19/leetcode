union-find    
每个cluster里有一个最高的root, weights[root] = 1.0, weights[a]/weights[root] = val.  
find 和 union的时候都要更新weights.   
find:   
if parents[a] != a, 找parents[a]的parent，同时更新weights[a] *= weights[parents[a]]. 因为find是recurvisely call，实际上是从离root最近的node开始更新weights，最后传递到a。   
例如: a/b = val1, b/root = val2   
现在parent[a] = b, parent[b] = c, parent[c] = c   
weights[a] = val1, weights[b] = val2, weights[c] = 1.0.   
最终wegihts[a]会被更新为val1 * val2 (a/c = val1*val2)   

union:  
a/c = weights[a]/weights[c], b/d = weights[b]/weights[d]  (这里c和d都是root)    
加入一条新的边， a/b = val  
先更新parent: parent[c] = d  
然后更新weights[c]:  
已知a/c = weights[a], b/d = weights[b]  
所以 c/d = (a/weights[a]) / (b/weights[b]) = a/b * weights[b] / weights[a] = val * weights[b] / weights[a]    
所以weights[p_a] = val * weights[b] / weights[a]   


最后query的时候，先find(a), find(b)，在这个过程中，a和b的weights都已经rescale成他们所在cluster的root的倍数了。判断a和b是否在一个cluster，如果在的话，return weights[a] / weights[b]   
