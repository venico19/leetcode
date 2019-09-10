# 输出任意一个valid解


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l_count = 0
        l_index = []
        remove_index = []
        for i, char in enumerate(s):
            if char == '(':
                l_index.append(i)
            elif char == ')':
                if not l_index:
                    remove_index.append(i)
                else:
                    l_index.pop()
                    
        remove_index += l_index
        remove_index = set(remove_index)
        res = ''
        for i, char in enumerate(s):
            if i not in remove_index:
                res += char
        return res
                