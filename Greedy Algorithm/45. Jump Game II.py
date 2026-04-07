class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0: return 0

        jumps = farthest = curr_end = 0

        for i in range(n-1):
            farthest = max(farthest, nums[i] + i)

            if i == curr_end:
                jumps += 1
                curr_end = farthest

                if curr_end >= n - 1:
                    break

        return jumps
