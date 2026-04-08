# Input = intervals = [[1,3],[2,6],[8,10],[15,18]]

class Solution(object):
    def merge(self, arr):
      res = []
      n = len(arr)
      i = 0

    while i < n:
        start = arr[i][0]
        end = arr[i][1]

        while i < n-1 and end >= arr[i + 1][0]:
            i += 1
            end = max(end, arr[i][0])
        res.append([start, end])
        i += 1

    return res
