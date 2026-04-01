class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        current_product = x  
        while n > 0:
            if n & 1:
                res *= current_product
            
            current_product *= current_product
            n >>= 1
            
        return res
