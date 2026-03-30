class Solution(object):
    def myAtoi(self, s):
        i = res = 0
        sign = 1
        n = len(s)

        while i < n and s[i] == ' ': 
            i += 1
        
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            sign = 1
            i += 1

        INT_MAX = 2**31 - 1
        INT_MIN = -2 ** 31

        while i < n and '0' <= s[i] <= '9':
            res = (res*10) + int(s[i])
            if res > INT_MAX:
                break
            i += 1

        res = res * sign

        if res > INT_MAX: return INT_MAX
        if res < INT_MIN: return INT_MIN

        return res
        
        
