class Solution:
    def checkIthBit(self, n, i):
        if (n >> i) & 1:
            return True
        else: 
            return False 
        
