class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxvalue = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxvalue or self.maxvalue[-1] <= x:
            self.maxvalue.append(x)

    def pop(self) -> int:
        val = self.stack.pop()
        if self.maxvalue and self.maxvalue[-1] == val:
            self.maxvalue.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxvalue[-1]

    def popMax(self) -> int:
        maxvalue = self.maxvalue.pop()
        temp = []
        while self.stack[-1] != maxvalue:
            temp.append(self.stack.pop())
        self.stack.pop()
        while temp:
            val = temp.pop()
            self.stack.append(val)
            if not self.maxvalue or self.maxvalue[-1] <= val:
                self.maxvalue.append(val)
        return maxvalue


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()