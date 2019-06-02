left: 剩余的没用的左括号数量   
right：剩余的没用的右括号数量    

为了保证valid，left == right的时候，下一个必须用左括号    
left < right的时候，下一个用谁都行（需要检查一下left是否为零）