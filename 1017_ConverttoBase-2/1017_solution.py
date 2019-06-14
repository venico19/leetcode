class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        
        res = ''
        digit = 0
        while N > 0:
            rem = N % (2 ** (digit + 1))
            if rem > 0:
                res += '1'
                N -= (-2) ** digit
            else:
                res += '0'
                
            digit += 1
            
        return res[::-1]
                