class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        i = n-1

        while i >= 0:
            if int(num[i]) % 2 == 1:
                return num[:i+1]
            else:
                i -= 1
        return ''

s = '35427'
obj = Solution()
print(obj.removeOuterParentheses(s))