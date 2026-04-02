class Solution:
    def nextSmallerElements(self, nums):
        # Your code goes here
        n = len(nums)
        ans = [-1] * n
        st = []

        for i in range(n -1, -1, -1):
            while st and st[-1] >= nums[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(nums[i])
        
        return ans
