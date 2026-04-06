# operation = [ "initializeheap", "insert", "insert", "insert", "getMin", "heapSize", "isEmpty", "extractMin", "changeKey" , "getMin" ]

class Solution():
  def initializeheap(self):
    self.capacity = 100
    self.size = 0
    self.arr = [0] * self.capacity

  def insert(self, x):
    if self.size == self.capacity:
      return

    self.size += 1
    i = self.size - 1
    self.arr[i] = x
    while i != 0 and self.arr[(i - 1) // 2] > self.arr[i]:
      self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
      i = (i - 1) // 2

  def extractMin(self):
    if self.size <= 0:
      return float('inf')
    if self.size == 1:
      self.size -= 1
      return self.arr[0]

    root = self.arr[0]
    self.arr[0] = self.arr[self.size - 1]
    self.size -= 1
    self.minHeapify(0)
    return root

  def minHeapify(self, i):
    l = i * 2 + 1
    r = i * 2 + 2
    smallest = i

    if l < self.size and self.arr[l] < self.arr[i]:
      smallest = l
    if r < self.size and self.arr[r] < self.arr[i]:
      smallest = r
    if i != smallest:
      self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
      self.minHeapify(smallest)

  def changeKey(self, index, new_val):
    if index > self.size:
      return 
    old_val = self.arr[index]
    self.arr[index] = new_val

    if old_val >= new_val:
      i = index
      while i != 0 and self.arr[(i - 1) // 2] > self.arr[i]:
        self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
        i = (i - 1) // 2
    else:
      self.minHeapify(i)
    
  def getMin(self):
    if self.size == 0:
      return float('inf')
    return self.arr[0]

  def heapSize(self):
    return self.size

  def isEmpty(self):
    return 1 if self.size == 0 else 0
