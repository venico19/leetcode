class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_res = []
            for l in res:
                n = len(l)
                for i in range(n + 1):
                    new_res.append(l[:i] + [num] + l[i:])
            res = new_res
            
        return res