class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        # longest sublist with at most 2 different values
        n = len(tree)
        res = 0
        left = 0
        freq = {}
        
        for i, num in enumerate(tree):
            freq[num] = freq.get(num, 0) + 1
            
            while len(freq) > 2:
                freq[tree[left]] -= 1
                if freq[tree[left]] == 0:
                    del freq[tree[left]]
                left += 1
                
            res = max(res, i - left + 1)
            
        return res
