class Solution(object):
    def numberOfSubstrings(self, s):
        # Frequency map for 'a', 'b', 'c'
        freq = [0, 0, 0]

        n = len(s)
        left = res = 0

        for right in range(n):
            freq[ord(s[right]) - ord('a')] += 1

            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                res += n - right
                freq[ord(s[left]) - ord('a')] -= 1 
                left += 1

        return res
