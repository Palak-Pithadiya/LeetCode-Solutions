class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        n = len(strs)
        m = len(strs[0])
        i = 0
        
        while i < m:
            pre = strs[0][i]
            j = 1
            while j < n:
                if i == len(strs[j]) or strs[j][i] != pre:
                    return strs[0][:i]
                j += 1
            i += 1

        return strs[0]
                
strs = ["flower","flow","flight"]
obj = Solution()
print(obj.longestCommonPrefix(s))