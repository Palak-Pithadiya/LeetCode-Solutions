import heapq

class Solution:
    def kthLargestElement(self, nums, k):
        if not nums or k > len(nums):
            return None

        self.heap = nums[:k]
        self.size = k

        for i in range((k // 2) - 1, -1, -1):
            self.minHeapify(i)

        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                self.heap[0] = nums[i]
                self.minHeapify(0)

        return self.heap[0]

    def minHeapify(self, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < self.size and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < self.size and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest],  self.heap[i]
            self.minHeapify(smallest)
