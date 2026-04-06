class Solution(object):
    def findContentChildren(self, greed, s):

        greed.sort()
        s.sort()
        n = len(greed)
        m = len(s)
        left = right = 0

        while left < m and right < n:
            if greed[right] <= s[left]:
                right += 1
            left += 1

        return right
