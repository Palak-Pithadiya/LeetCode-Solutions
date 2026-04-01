class Solution:   
    def singleNumber(self, nums):
        #your code goes here
        xorAll = 0
        for n in nums:
            xorAll ^= n

        rightMostBit = xorAll & -xorAll
        a, b = 0, 0
        for n in nums:
            if n & rightMostBit:
                a ^= n
            else:
                b ^= n

        return sorted([a, b])
