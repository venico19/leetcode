class Solution:
    def isNumber(self, s: str) -> bool:
        # remove space at begin and at end
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        s = s[i:]
        
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        s = s[:i+1]

        if not s:
            return False
        
        return self.isInt(s) or self.isFloat(s) or self.isExp(s)
        
    def isUnsignedInt(self, s):
        if not s:
            return False
        for char in s:
            if char not in '0123456789':
                return False
        return True
    
    def isSignedInt(self, s):
        if not s:
            return False
        return s[0] in '+-' and self.isUnsignedInt(s[1:])
        
    def isInt(self, s):
        return self.isUnsignedInt(s) or self.isSignedInt(s)
    
    def isUnsignedFloat(self, s):
        if not s or s == '.':
            return False
        split = s.split('.')
        if len(split) != 2:
            return False
        return (self.isInt(split[0]) or split[0] == '') \
            and (self.isUnsignedInt(split[1]) or split[1] == '')

    def isSignedFloat(self, s):
        if not s:
            return False
        return s[0] in '+-' and self.isUnsignedFloat(s[1:])
        
    def isFloat(self, s):
        return self.isUnsignedFloat(s) or self.isSignedFloat(s)
    
    def isExp(self, s):
        if not s or s == 'e':
            return False
        split = s.split('e')
        if len(split) != 2:
            return False
        return (self.isFloat(split[0]) or self.isInt(split[0])) \
            and self.isInt(split[1])
        