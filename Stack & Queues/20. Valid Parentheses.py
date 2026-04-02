class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        for i in range(len(s)):
            char = s[i]

            if char == '(' or char == '{' or char == '[':
                st.append(char)
            else:
                if not st:
                    return False
                ch = st.pop()
                if char == ')' and ch != '(':
                    return False
                elif char == '}' and ch != '{':
                    return False
                elif char == ']' and ch != '[':
                    return False

        return True if not st else False
