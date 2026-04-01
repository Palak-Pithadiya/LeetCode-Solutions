class ArrayQueue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.arr = [0]*1000

    def push(self, x):
        if self.start == -1:
            self.start += 1
            self.end += 1
            self.arr[self.start] = x
        else:
            self.end += 1
            self.arr[self.end] = x

    def pop(self):
        if self.start == -1:
            return -1
        
        val = self.arr[self.start]

        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            self.start += 1
        return val

    def peek(self):
        if self.start == -1:
            return -1
        return self.arr[self.start]

    def isEmpty(self):
        return self.start == -1
