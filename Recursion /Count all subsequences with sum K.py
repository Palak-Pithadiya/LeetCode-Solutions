class Solution:
    def SubsequenceSum(self, index, currentSum, target, arr):
        if index == len(arr): 
            if currentSum == target: return 1
            else: return 0

        currentSum += arr[index]
        left = self.SubsequenceSum(index + 1, currentSum, target, arr)

        currentSum -= arr[index]
        right = self.SubsequenceSum(index + 1, currentSum, target, arr)

        return left + right

    def countSubsequenceWithTargetSum(self, nums, k):
        currentSum = index = 0
        return self.SubsequenceSum(index, currentSum, k, nums)
