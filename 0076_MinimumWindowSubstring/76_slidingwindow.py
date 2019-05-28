class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = self.counter(t)

        window = {}
        complete = set()
        
        n = len(s)
        l, r = 0, 0
        res_l, res_r = -1, n
        
        for r, char in enumerate(s):
            if char not in counter_t:
                continue
                
            window[char] = window.get(char, 0) + 1
            if window[char] >= counter_t[char]:
                complete.add(char)
            while len(complete) == len(counter_t):
                if r - l < res_r - res_l:
                    res_l, res_r = l, r
                if s[l] in counter_t:
                    window[s[l]] -= 1
                    if window[s[l]] < counter_t[s[l]]:
                        complete.remove(s[l])
                l += 1
        
        if res_l == -1:
            return ''
        else:
            return s[res_l:res_r+1]
        
    def counter(self, s):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        return d