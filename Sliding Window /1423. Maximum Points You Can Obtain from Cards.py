class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        maxPoint = total

        for i in range(k):
            # Subtract from the front
            total -= cardPoints[k - 1 - i]

            # Add from the back
            total += cardPoints[n - 1 - i]

            maxPoint = max(maxPoint, total)

        return maxPoint
