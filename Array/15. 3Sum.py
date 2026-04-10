class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        i = 0

        while i < n:
            while i > 0 and i < n and nums[i] == nums[i - 1]:
                i += 1
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp < 0:
                    j += 1
                elif temp > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1

        return res
