class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = maxOnce = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else: 
                count = 0
            
            maxOnce = max(maxOnce, count)

        return maxOnce
