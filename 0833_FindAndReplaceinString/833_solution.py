class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        if not indexes:
            return S
        
        sorted_indexes = []
        for i, indexes in enumerate(indexes):
            sorted_indexes.append((indexes, i))
        sorted_indexes.sort()

        res = ''
        start = 0
        for index, i in sorted_indexes:
            source_length = len(sources[i])
            target_length = len(targets[i])
            res += S[start:index]
            start = index
            
            if S[index:index + source_length] == sources[i]:
                res += targets[i]
                start = index + source_length
                
        res += S[start:]
        
        return res