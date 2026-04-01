class ArrayStack:
    def __init__(self):
        self.top_idx = -1
        self.arr = [0] * 1000

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
        if self.top_idx == -1:
            return -1
        return self.arr[self.top_idx]

    def isEmpty(self):
        if self.top_idx == -1:
            return True
        else: return False
