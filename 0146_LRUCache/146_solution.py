class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # use double linked list to maintain LRU node
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return self.cache[key].value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache.keys()) > self.capacity:
            delNode = self.head.next
            del self.cache[delNode.key]
            self._remove(delNode)
        
    def _add(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.next = self.tail
        node.prev = lastNode
        self.tail.prev = node
        
    def _remove(self, node):
        prevNode = node.prev
        prevNode.next = node.next
        node.next.prev = prevNode

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)