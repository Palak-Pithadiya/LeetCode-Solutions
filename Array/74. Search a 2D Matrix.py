class Solution(object):
    def searchMatrix(self, mat, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not mat or not mat[0]:
            return False

        n = len(mat)
        m = len(mat[0])

        i = 0
        j = n - 1

        while i <= j:
            mid_row = (i + j) // 2
            left = 0
            right = m - 1
            if mat[mid_row][left] <= target and mat[mid_row][right] >= target:
                while left <= right:
                    mid = (left + right) // 2
                    if mat[mid_row][mid] == target:
                        return True
                    elif mat[mid_row][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
                
            elif mat[mid_row][left] > target:
                j = mid_row - 1
            else:
                i = mid_row + 1

        return False
