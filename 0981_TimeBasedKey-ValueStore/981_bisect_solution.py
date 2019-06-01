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
        loc = bisect.bisect_right(self.dict[key][0], timestamp)
        if loc == 0:
            return ''
        else:
            return self.dict[key][1][loc-1]
