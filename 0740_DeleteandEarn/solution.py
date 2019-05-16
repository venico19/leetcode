class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        uniNums = sorted(counter.keys())     
        uniNums = [-1] + uniNums
        
        n = len(uniNums)
        # pick[i]: max score of uniNums[:i], pick uniNums[i]
        # avoid[i]: max score of uniNums[:i], avoid uniNums[i]
        pick = [0 for _ in range(n)]
        avoid = [0 for _ in range(n)]
                
        for i in range(1, n):
            if uniNums[i] > uniNums[i - 1] + 1:
                pick[i] = max(pick[i - 1], avoid[i - 1]) + uniNums[i] * counter[uniNums[i]]
            else:
                pick[i] = max(pick[i - 2], avoid[i - 2]) + uniNums[i] * counter[uniNums[i]]
            avoid[i] = max(pick[i-1], avoid[i-1])

        return max(avoid[-1], pick[-1])
            
