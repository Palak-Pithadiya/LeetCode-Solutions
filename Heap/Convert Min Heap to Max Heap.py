class Solution:
    def minToMaxHeap(self, nums):
        n = len(nums)
        if n <= 1:
            return nums

        for i in range((n // 2) - 1, -1, -1):
            self.maxHeapify(nums, n, i)

        return nums

    def maxHeapify(self, nums, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxHeapify(nums, n, largest)
