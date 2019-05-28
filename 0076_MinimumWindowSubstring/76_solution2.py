class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = {}
        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1
            
        filtered_s = []
        for i, char in enumerate(s):
            if char in counter_t:
                filtered_s.append((i, char))

        n = len(s)
        l = 0
        res_l, res_r = -1, n
        window = {}
        complete = set()
        
        for (r, char) in filtered_s:
            window[char] = window.get(char, 0) + 1
            if window[char] == counter_t[char]:
                complete.add(char)
                
            while len(complete) == len(counter_t):
                if r - filtered_s[l][0] < res_r - res_l:
                    res_l, res_r = filtered_s[l][0], r
                left_char = filtered_s[l][1]
                window[left_char] -= 1
                if window[left_char] < counter_t[left_char]:
                    complete.remove(left_char)
                l += 1
                
        if res_l == -1:
            return ''
        else:
            return s[res_l:res_r+1]