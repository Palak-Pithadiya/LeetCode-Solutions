class Solution:
    def count_NGE(self, nums, indices):
        # Your code goes here
        n = len(nums)
        ans = []

        for idx in indices:
            count = 0
            currEle = nums[idx]

            for j in range(idx + 1, n):
                if nums[j] > currEle:
                    count += 1
            ans.append(count) 
        return ans
