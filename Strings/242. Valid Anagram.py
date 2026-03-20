class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s = {}

        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]] += 1
            else:
                map_s[s[i]] = 1

        for i in range(len(t)):
            if (t[i] not in map_s) or (map_s[t[i]] - 1) == -1:
                return False
            map_s[t[i]] -= 1            

        return True

s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s, t))
