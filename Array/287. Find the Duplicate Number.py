class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        j = i + 1
        
        while j < len(nums):
            if nums[i] == nums[j]:
                return nums[i]
            i += 1
            j = i + 1
