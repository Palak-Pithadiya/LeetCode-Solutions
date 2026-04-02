class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res_map = {}
        st = []

        for num in nums2:
            while st and num > st[-1]:
                popped_val = st.pop()
                res_map[popped_val] = num
            
            st.append(num)

        ans = []
        for num in nums1:
            if num in res_map:
                ans.append(res_map[num])
            else:
                ans.append(-1)

        return ans 
