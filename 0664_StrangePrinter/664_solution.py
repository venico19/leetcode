class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        
        shorten = ""
        for i, char in enumerate(s):
            if i > 0 and char == shorten[-1]:
                continue
            shorten += char
                    
        s = shorten
        
        lookup = {}
        for i, char in enumerate(s):
            if char not in lookup:
                lookup[char] = []
            lookup[char].append(i)

        memo = {}
        
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= j:
                memo[(i, j)] = 0
                return 0
            if j - i == 1:
                memo[(i, j)] = 1
                return 1
            
            tail = s[j-1]
            res = float("Inf")
            for index in lookup[tail]:
                if index < i:
                    continue
                if index >= j-1:
                    break
                # if find such index, print from index to j - 1
                res = min(res, helper(i, index + 1) + 1 + helper(index + 1, j - 1))
                
            # or print tail char seperately
            res = min(res, helper(i, j - 1) + 1)
            
            memo[(i, j)] = res
            return memo[(i, j)]        
            
        return helper(0, len(s))
