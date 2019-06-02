class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        visited = {beginWord: [beginWord]}
        
        queue = collections.deque()
        queue.append((beginWord, 1))
        
        while queue:
            w, depth = queue.popleft()
            for transform in self.wordTransform(w):
                if transform in visited:
                    continue
                if transform in wordSet:
                    visited[transform] = visited[w] + [transform]
                    if transform == endWord:
                        return depth + 1
                    queue.append((transform, depth + 1))
        return 0
    
    def wordTransform(self, word):
        res = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                res.append(word[:i] + char + word[i+1:])
        return res
    