class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        self.temp = Node(x)
        self.temp.next = self.head
        self.head = self.temp
        self.size += 1

    def pop(self):
        if self.isEmpty(): return -1

        val = self.head.data
        self.head = self.head.next
        self.size -= 1

        return val

    def top(self):
        return self.head.data if self.head != None else -1

    def isEmpty(self):
        if self.head == None:
            return True
        else: 
            return False
