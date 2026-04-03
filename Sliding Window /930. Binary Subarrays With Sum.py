class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atMost(target):
            if target < 0:
                return 0

            left = count = currSum = 0
            for right in range(len(nums)):
                currSum += nums[right]

                while currSum > target:
                    currSum -= nums[left]
                    left += 1

                count += (right - left + 1)

            return count

        return atMost(goal) - atMost(goal - 1)
