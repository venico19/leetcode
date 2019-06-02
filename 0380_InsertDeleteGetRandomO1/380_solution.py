import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.total = 0
        self.nums = []
        self.position = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.position:
            return False
        self.position[val] = self.total
        self.total += 1
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.position:
            return False
        index = self.position[val]
        tail_val = self.nums[-1]
        
        # update self.nums
        self.nums[index] = tail_val
        self.nums.pop()
        
        # update self.position
        self.position[tail_val] = index
        del self.position[val]
        
        # update self.total
        self.total -= 1
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.total == 0:
            return None
        return self.nums[random.randint(0, self.total - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()