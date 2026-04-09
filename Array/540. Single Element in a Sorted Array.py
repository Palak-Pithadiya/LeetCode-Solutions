class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        if high == 0:
            return nums[0]

        while low <= high:
            mid = (low + high) // 2

            left_is_different = (mid == 0 or nums[mid] != nums[mid - 1])
            right_is_different = (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])

            if left_is_different and right_is_different:
                return nums[mid]

            elif (mid%2 == 0 and nums[mid] == nums[mid + 1]) or (mid%2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1

            else:
                high = mid - 1
