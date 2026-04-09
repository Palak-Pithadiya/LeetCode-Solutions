class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        max_so_far = curr_sum = nums[0]

        for i in range(1, n):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]

            max_so_far = max(max_so_far, curr_sum)
            
        return max_so_far
