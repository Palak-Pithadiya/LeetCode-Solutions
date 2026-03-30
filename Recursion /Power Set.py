class Solution:
    def helper(self, s, index, curr, result):
        if index == len(s):
            result.append(list(curr))
            return

        self.helper(s, index + 1, curr, result)

        curr.append(s[index])
        self.helper(s, index + 1, curr, result)
        curr.pop()

    def powerSet(self, nums):
        #your code goes here
        current, result = [], []
        self.helper(nums, 0, current, result)
        return result
