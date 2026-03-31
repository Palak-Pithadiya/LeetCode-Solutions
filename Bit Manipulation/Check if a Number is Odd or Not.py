class Solution:
    def isOdd(self, n: int) -> bool:
        # Your code goes here
        if(n & 1 == 1):
            return True
        else:
            return False

"""
let n = 13

  n = 1 0 1 1 
& 1 = 0 0 0 1
--------------
      0 0 0 1
"""
