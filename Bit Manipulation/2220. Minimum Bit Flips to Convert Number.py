class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        res = start ^ goal
        cnt = 0

        while res:
            res &= (res - 1)
            cnt += 1

        return cnt
