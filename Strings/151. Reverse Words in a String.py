class Solution(object):
    def reverseWords(self, s):
        n = len(s)
        ans = ''
        i = 0

        while i < n:
            while i < n and s[i] == " ":
                i += 1

            if i >= n: break

            word = ''
            while i < n and s[i] != ' ':
                word += s[i]
                i += 1

            if ans == '':
                ans = word
            else:
                ans = word + " " + ans

        return ans
        
s = "the sky is blue"
obj = Solution()
print(obj.reverseWords(s))