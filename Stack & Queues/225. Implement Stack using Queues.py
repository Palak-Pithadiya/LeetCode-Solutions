class ArrayQueue(object):
    def __init__(self):
        self.arr = [0]*1000
        self.start = self.end = self.size = 0

    def push(self, x):
        self.arr[self.end] = x
        self.end += 1
        self.size += 1  

    def pop(self):
        if self.size == 0:
            return -1
        val = self.arr[self.start]
        self.start += 1
        self.size -= 1
        return val

    def peek(self):
        if self.size > 0:
            return self.arr[self.start]
        return -1

class MyStack(object):
    def __init__(self):
        self.q1 = ArrayQueue()
        self.q2 = ArrayQueue()

    def push(self, x):
        self.q1.push(x)
        
    def pop(self):
        if self.q1.size == 0:
            return -1

        while self.q1.size > 1:
            self.q2.push(self.q1.pop())

        val = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self):
        if self.q1.size == 0:
            return -1

        while self.q1.size > 1:
            self.q2.push(self.q1.pop())

        val = self.q1.pop()
        self.q2.push(val)

        self.q1, self.q2 = self.q2, self.q1
        return val

    def empty(self):
        return self.q1.size == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
