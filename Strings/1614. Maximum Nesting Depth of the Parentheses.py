class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = p = 0
        
        for i in s:
            if i == '(':
                p += 1
            elif i == ')':
                p -= 1
            ans = max(ans, p)

        return ans
        
s = "(1+(2*3)+((8)/4))+1"
obj = Solution()
print(obj.maxDepth(s))
