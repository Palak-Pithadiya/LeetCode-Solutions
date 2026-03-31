class Solution:
    def countSetBits(self, n: int) -> int:
        # Your code goes here
        cnt = 0
        while n != 1:
            cnt += (n & 1) # (n % 2)
            n = n >> 1 # n //= 2

        if n == 1: 
            cnt += 1

        return cnt
