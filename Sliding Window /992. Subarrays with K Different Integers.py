class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            freq = {}
            left = count = 0

            for right in range(len(nums)):
                if nums[right] not in freq or freq[nums[right]] == 0:
                    k -= 1
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while k < 0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        k += 1
                    left += 1
                count += (right - left + 1)

            return count

        return atMost(k) - atMost(k - 1)
