class ArrayStack():
    def __init__(self):
        self.arr = [0]*1000
        self.top_idx = -1

    def push(self, x):
        self.top_idx += 1
        self.arr[self.top_idx] = x

    def pop(self):
        if self.top_idx == -1:
            return -1
        val = self.arr[self.top_idx]
        self.top_idx -= 1
        return val

    def top(self):
        return self.arr[self.top_idx]

    def isEmpty(self):
        return self.top_idx == -1

class MyQueue(object):
    def __init__(self):
        self.s1 = ArrayStack()
        self.s2 = ArrayStack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        self.shift_stacks()
        return self.s2.pop()

    def peek(self):
        self.shift_stacks()
        return self.s2.top()
        
    def empty(self):
        return self.s1.isEmpty() and self.s2.isEmpty() 

    def shift_stacks(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
