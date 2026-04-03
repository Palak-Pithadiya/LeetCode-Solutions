class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7

        arr = [0] + arr + [0]
        res = 0
        stack = []
        
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] > arr[i]:
                mid = stack.pop()
                left = stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                res += count * arr[mid]

            stack.append(i)

        return res % mod
