class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        def backTrack(index, ds):
            ans.append(list(ds))

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue

                ds.append(nums[i])
                backTrack(i + 1, ds)

                ds.pop()

        backTrack(0, [])
        return ans
