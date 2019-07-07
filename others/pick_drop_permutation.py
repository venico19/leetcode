"""
https://www.1point3acres.com/bbs/thread-531559-1-1.html
Input：一个list，里面是pair<pickup_city, dropoff_city>, 先pick后drop
Output: 输出所有的可能顺序

Ex. <a_pick, b_drop>, <b_pick, a_drop>
output: 
a_pick, b_drop, b_pick, a_drop
a_pick, b_pick, a_drop, b_drop
b_pick, a_drop, a_pick, b_drop
b_pick, a_pick, a_drop, b_drop 
....... 1point3acres

Follow up: optimize time complexity
"""

def trip(l):
    n = len(l)
    res = []

    def permutation(start, prev):
        if start == n:
            res.append(prev)
            return
        [pickup, dropoff] = l[start]
        k = len(prev)
        for i in range(k+1):
            for j in range(i, k+1):
                ans = prev[:i] + [pickup] + prev[i:j] + [dropoff] + prev[j:]
                permutation(start + 1, ans)

    permutation(0, [])
    return res

def trip2(l, capacity):
    N = len(l)
    res = []

    def backtracking(available_pick, available_drop, count, prev_path):
        if len(prev_path) == 2*N:
            res.append(prev_path)
            return 
        for i in range(N):
            if available_drop[i] == 1:
                available_drop[i] = 0
                backtracking(available_pick, available_drop, count - 1, prev_path + [l[i][1]])
                available_drop[i] = 1

        if count < capacity:
            for i in range(N):
                if available_pick[i] == 1:
                    available_pick[i] = 0
                    available_drop[i] = 1
                    backtracking(available_pick, available_drop, count + 1, prev_path + [l[i][0]])
                    available_drop[i] = 0
                    available_pick[i] = 1

    available_pick = [1 for _ in range(N)]
    available_drop = [0 for _ in range(N)]
    backtracking(available_pick, available_drop, 0, [])
    return res

if __name__ == "__main__":
    l = [['a', 'b'], ['c', 'd']]
    #print(trip(l))
    print(trip2(l, 1))