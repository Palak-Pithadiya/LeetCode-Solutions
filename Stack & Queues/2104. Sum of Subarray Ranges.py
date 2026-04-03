class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def get_max(is_max):
            res = 0
            stack = []

            arr = [float('inf') if is_max else float('-inf')] + nums + [float('inf') if is_max else float('-inf')]

            for i, val in enumerate(arr):
                while stack and (arr[stack[-1]] < val if is_max else arr[stack[-1]] > val):
                    mid = stack.pop()
                    left = stack[-1]
                    right = i 
                    res += arr[mid] * (mid - left) * (right - mid)
                stack.append(i)

            return res

        return get_max(True) - get_max(False) 
