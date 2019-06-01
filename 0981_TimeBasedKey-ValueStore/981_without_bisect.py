class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [[],[]]
        self.dict[key][0].append(timestamp)
        self.dict[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ''
        loc = self.binary_search(timestamp, self.dict[key][0])
        if loc == 0 and self.dict[key][0][0] > timestamp:
            return ''
        else:
            return self.dict[key][1][loc]
        
    def binary_search(self, target, l):
        # return the location to insert target
        n = len(l)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if l[mid] == target:
                return mid
            elif l[mid] > target:
                right = mid - 1
            else:
                if mid + 1 < n and l[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1
        return left
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)