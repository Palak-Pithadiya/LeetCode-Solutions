class Solution:
    def subsetSums(self, nums):
        #your code goes here
        sums = []
        n = len(nums)
        def findSums(index, currSum):
            if index == n:
                sums.append(currSum)
                return
            
            findSums(index + 1, currSum + nums[index])
            findSums(index + 1, currSum)

        findSums(0, 0)
        sums.sort()
        return sums
