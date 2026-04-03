class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        freq = [0] * 26
        maxLen = maxCount = left = 0

        for right in range(n):

            freq[ord(s[right]) - ord('A')] += 1
            maxCount = max(maxCount, freq[ord(s[right]) - ord('A')])

            while(right - left + 1) - maxCount > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLen = max(right - left + 1, maxLen)

        return maxLen
