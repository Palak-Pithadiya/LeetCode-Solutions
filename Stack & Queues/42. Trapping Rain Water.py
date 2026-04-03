class Solution(object):
    def trap(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        if not arr:
            return 0

        left = 0
        right = len(arr) - 1
        l_max = arr[left]
        r_max = arr[right]
        water = 0

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, arr[left])
                water += (l_max - arr[left])
            else:
                right -= 1
                r_max = max(r_max, arr[right])
                water += (r_max - arr[right])

        return water
