class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1]*n
        st = []

        for i in range(2*n):
            curr_idx = i % n

            while st and nums[curr_idx] > nums[st[-1]]:
                popped_idx = st.pop()
                res[popped_idx] = nums[curr_idx]

            if i < n:
                st.append(i)

        return res
