import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.array = self.original[:]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.array)
        for i in range(n):
            swap_index = random.randint(i, n - 1)
            self.array[i], self.array[swap_index] = self.array[swap_index], self.array[i]
            
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()