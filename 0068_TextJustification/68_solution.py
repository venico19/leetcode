class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line = []
        line_len = 0
        for word in words:
            word_len = len(word)
            if line_len == 0:
                line.append(word)
                line_len += word_len
            elif line_len > 0 and line_len + 1 + word_len <= maxWidth: 
                # 1 is the length for space before w
                line.append(word)
                line_len += word_len + 1
            else:
                # line is full, add it to res
                res.append(self.listToString(line, maxWidth))
                line = [word]
                line_len = word_len
       
        # add last line
        last_line = line[0]
        for word in line[1:]:
            last_line += ' '
            last_line += word
        while len(last_line) < maxWidth:
            last_line += ' '
        
        res.append(last_line)
        
        return res
                
    def listToString(self, l, maxWidth):
        n = len(l)
        if n == 1:
            res = l[0]
            while len(res) < maxWidth:
                res += ' '
        else:
            length = 0
            for word in l:
                length += len(word)
            length += n - 1     # space
            
            # number of space between words
            spaces = [1 for _ in range(n-1)]
            i = 0
            while length < maxWidth:
                spaces[i] += 1
                length += 1
                i += 1
                if i == n - 1:
                    i = 0
                    
            res = l[0]
            for i in range(n - 1):
                res += ' ' * spaces[i]
                res += l[i+1]
                
        return res