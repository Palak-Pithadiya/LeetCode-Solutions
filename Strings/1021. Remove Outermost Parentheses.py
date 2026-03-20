class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ''
        counter = 0

        for i in s:
            if counter == 0:
                counter += 1
            elif i == '(':
                counter += 1
                string += i
            elif i == ')':
                if counter - 1 == 0:
                    counter -= 1
                else:
                    counter -= 1
                    string += i       
        
        return string
    
s = "(()())(())"
obj = Solution()
print(obj.removeOuterParentheses(s))