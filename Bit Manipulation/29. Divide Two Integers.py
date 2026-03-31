class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1

        sign = 1
        if((dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0)):
            sign = -1

        n = abs(dividend)
        d = abs(divisor)
        ans = 0

        while n >= d:
            cnt = 0

            # d << (cnt + 1) == d * (2^(cnt + 1))
            while n >= (d << (cnt + 1)):
                cnt += 1

            # 1 << cnt == 2 ^ cnt
            ans += (1 << cnt)
            n -= (d << cnt)

        ans = sign * ans

        if ans > 2**31 - 1 :
            return 2**31 - 1
        if ans < -2**31:
            return -2**31

        return ans
