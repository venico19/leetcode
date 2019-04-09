class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []
        
        # trie
        trie = {}
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            # '#' is end of word
            t['#'] = {}
        
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = set()
        
        def search(i, j, trie, path):
            if '#' in trie:
                res.add(path)
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if not visited[i][j] and board[i][j] in trie:
                visited[i][j] = True
                search(i+1, j, trie[board[i][j]], path + board[i][j])
                search(i-1, j, trie[board[i][j]], path + board[i][j])
                search(i, j+1, trie[board[i][j]], path + board[i][j])
                search(i, j-1, trie[board[i][j]], path + board[i][j])
                visited[i][j] = False
                
        for i in range(m):
            for j in range(n):
                search(i, j, trie, "")
                
        return list(res)
    
        
