class MinStack(object):

    def __init__(self):
        self.arr = []
        self.top_idx = -1

    def push(self, val):
        if self.top_idx == -1:
            currentMin = val
        else:
            currentMin = min(val, self.getMin())
        self.arr.append([val, currentMin])
        self.top_idx += 1

    def pop(self):
        if self.top_idx == -1: 
            return -1
        val = self.arr.pop()
        self.top_idx -= 1
        return val[0]

    def top(self):
        if self.top_idx == -1: 
            return -1
        return self.arr[self.top_idx][0]

    def getMin(self):
        if self.top_idx == -1: 
            return -1

        top_pair = self.arr[self.top_idx]
        return top_pair[1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
