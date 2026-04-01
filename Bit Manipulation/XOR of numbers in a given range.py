class Solution:      
    def findRangeXOR(self, l, r):
        #your code goes here
        def xorTillN(n):
            mod = n % 4
            if mod == 0: return n
            if mod == 1: return 1
            if mod == 2: return n + 1
            return 0

        return xorTillN(n-1) ^ xorTillN(r)
