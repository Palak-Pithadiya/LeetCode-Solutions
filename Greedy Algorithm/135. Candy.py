class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        can = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                can[i] = can[i - 1] + 1

        # Right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                can[i] = max(can[i], can[i + 1] + 1)

        return sum(can)
