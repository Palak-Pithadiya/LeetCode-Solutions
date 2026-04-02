class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.size = 0

    def push(self, x):
        self.temp = Node(x)

        if self.head is None:
            self.head = self.temp
            self.tail = self.temp
        else:
            self.tail.next = self.temp
            self.tail = self.temp

    def pop(self):
        if self.isEmpty(): return -1

        val = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
            
        return val

    def peek(self):
        if self.isEmpty(): return -1
        return self.head.data

    def isEmpty(self):
        return self.head is None
