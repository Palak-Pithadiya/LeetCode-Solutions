class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr_sum = 0

        prefix_sum = {0: 1}

        for num in nums:
            current_sum += num

            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count
