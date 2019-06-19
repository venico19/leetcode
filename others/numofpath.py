#机器人高频面经 一个M*N格子 从 (0,0) 到（M，0）x方向+1 y方向{-1,0,+1}问有多少path
#followup1 假设要经过一个点（A，B ）问有多少种path
#followup2 假设要经过一些点
#followup3 假设path要穿过x=h

def dfs_solution(M, N):
    res = [0]
    def dfs(i, j, visited):
        if i < 0 or i >= M or j < 0 or j >= N or (i, j) in visited:
            return
        if i == M - 1 and j == 0:
            res[0] += 1
            return
        visited.add((i, j))
        dfs(i, j + 1, visited)
        dfs(i, j - 1, visited)
        dfs(i + 1, j, visited)
        visited.remove((i, j))

    dfs(0, 0, set())
    return res[0]

def dp_solution(M, N):
    dp = [[0 for _ in range(N)] for _ in range(M)]
    for j in range(N):
        dp[0][j] = 1
    for i in range(1, M):
        dp[i][0] = dp[i-1][0]
        for j in range(1, N):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        cumSum = dp[i-1][N-1]
        for j in range(N - 2, -1, -1):
            dp[i][j] += cumSum
            cumSum += dp[i-1][j]
    print(dp)
    return dp[M-1][0]

if __name__ == '__main__':
    print(dfs_solution(4, 4))
    print(dp_solution(4, 4))

