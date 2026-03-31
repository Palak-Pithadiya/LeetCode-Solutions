class Solution:
    def Subsequence(self, index, currentSum, target, arr):
        if index == len(arr):
            return currentSum == target

        if(self.Subsequence(index + 1, currentSum + arr[index], target, arr)):
            return True
        if(self.Subsequence(index + 1, currentSum, target, arr)):
            return True

        return False

    def checkSubsequenceSum(self, nums, k):
        #your code goes here
        if(self.Subsequence(0, 0, k, nums)):  return "Yes"
        else: return "No"
