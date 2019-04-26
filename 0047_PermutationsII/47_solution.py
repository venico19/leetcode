class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_res = []
            for l in res:
                n = len(l)
                for i in range(n + 1):
                    new_res.append(l[:i] + [num] + l[i:])
                    if i < n and l[i] == num:
                        break
                    
            res = new_res
        
        return res