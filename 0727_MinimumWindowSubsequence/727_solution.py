class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)
        dp = [-1 for _ in range(n)]
        for i, char in enumerate(S):
            if T[0] == char:
                dp[i] = i
      
        for j in range(1, len(T)):
            new = [-1 for _ in range(n)]
            lastseen = -1
            for i, char in enumerate(S):
                if lastseen != -1 and char == T[j]:
                    new[i] = lastseen
                if dp[i] > -1:
                    lastseen = dp[i]
            dp = new
            
        left, right = 0, n
        for end, start in enumerate(dp):
            if start != -1 and end - start < right - left:
                left, right = start, end
       
        return S[left:right+1] if right < n else ''
                    