class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        hashLen = 256

        hash = [-1] * hashLen
        left = right = maxLen = 0

        while right < n:
            if(hash[ord(s[right])] != -1):
                left = max(hash[ord(s[right])] + 1, left)
            calculateLen = right - left + 1
            maxLen = max(calculateLen, maxLen)

            hash[ord(s[right])] = right
            right += 1

        return maxLen
