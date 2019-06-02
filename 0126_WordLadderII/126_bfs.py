class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList:
            return []
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        path = {beginWord:(1, [[beginWord]])}
        queue = collections.deque()
        queue.append((beginWord, 1))
        
        while queue:
            w, depth = queue.popleft()
            for t in self.wordTransform(w):
                if t not in wordSet:
                    continue
                if t in path and path[t][0] < depth + 1:
                    continue
                if not t in path:
                    queue.append((t, depth + 1))
                if t not in path:
                    path[t] = (depth + 1, [])
                for p in path[w][1]:
                    path[t][1].append(p + [t])
                    
            if endWord in path and depth + 1 > path[endWord][0]:
                return path[endWord][1]
        
        if endWord in path:
            return path[endWord][1]
        else:
            return []
            
    def wordTransform(self, w):
        n = len(w)
        res = []
        for i in range(n):
            for char in string.ascii_lowercase:
                if char == w[i]:
                    continue
                res.append(w[:i] + char + w[i+1:])
        return res        