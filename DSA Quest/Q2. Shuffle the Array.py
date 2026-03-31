# Optimal approach
# Time complexity = o(n)
class Solution(object):
    def shuffle(self, nums, n):
        ans = [0] * (2 * n)

        for i in range(n):
            ans[2 * i] = nums[i]
            ans[2 * i + 1] = nums[n + i]

        return ans


# Better approach
# Time complexity = o(n^2)
class Solution(object):
    def shuffle(self, nums, n):
        if n == 1:
            return nums

        l = len(nums)
        for i in range(n):
            temp = nums[n + i]

            j = (i * 2) + 1
            k = (n + i)
            while k > j:
                nums[k] = nums[k-1]
                k -= 1
            nums[k] = temp
        return nums
