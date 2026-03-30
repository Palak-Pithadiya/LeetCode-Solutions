class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7

        def power(x, y):
            if y == 0:
                return 1

            half = power(x, y//2)

            if y % 2 == 0:
                return (half * half) % mod
            else:
                return (x * half * half) % mod

        even_pos = (n + 1) // 2
        odd_pos = n // 2

        ans_even = power(5, even_pos)
        ans_odd = power(4, odd_pos)

        return (ans_even * ans_odd) % mod
        
