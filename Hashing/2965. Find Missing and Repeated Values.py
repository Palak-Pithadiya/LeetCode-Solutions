class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        size = n * n
        count = [0] * (size + 1)

        for row in grid:
            for val in row:
                count[val] += 1

        a, b = -1, -1 
        for i in range(1, size+1):
            if count[i] == 2:
                a = i
            elif count[i] == 0:
                b = i

        return [a, b]
