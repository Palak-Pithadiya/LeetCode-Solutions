class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in map_s:
                if map_s[char_s] != char_t:
                    return False
            else:
                map_s[char_s] = char_t

            if char_t in map_t:
                if map_t[char_t] != char_s:
                    return False
            else:
                map_t[char_t] = char_s

        return True
                
s = "egg"
t = "add"
obj = Solution()
print(obj.isIsomorphic(s, t))
