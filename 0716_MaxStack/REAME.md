**solution 1: temp stack**  
用stack记录所有value，用maxvalue记录当前最大值  
popMax之后把stack顶端比maxvalue小的值都挪到一个temp stack里，等pop了max之后，再把temp stack里的值移回去，同时也要更新maxvalue里的最大值。  