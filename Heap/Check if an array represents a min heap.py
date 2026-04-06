class Solution:
    def isHeap(self, nums):
        n = len(nums)
        for i in range(n // 2):
            l = 2 * i + 1
            r = 2 * i + 2

            if nums[i] > nums[l]:
                return False

            if r < n and nums[i] > nums[r]:
                return False
        return True
