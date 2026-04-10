class Solution(object):
    def merge(self, arr):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not arr:
            return []

        arr.sort(key = lambda x: x[0])
        n = len(arr)
        res = []
        i = 0

        while i < n:
            start = arr[i][0]
            end = arr[i][1]
            while i < (n-1) and end >= arr[i + 1][0]:
                end = max(end, arr[i + 1][1])
                i += 1
            res.append([start, end])
            i += 1

        return res
