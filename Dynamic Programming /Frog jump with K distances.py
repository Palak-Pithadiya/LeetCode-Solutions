class Solution:
    def frogJump(self, heights, k):
        n = len(heights)

        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = 0
        
        for i in range(1, n):
            min_step = float('inf')

            for j in range(1, k + 1):
                if i - j >= 0:
                    jump_energy = dp[i - j] + abs(heights[i] - heights[i - j])
                    min_step = min(min_step, jump_energy)
                else:
                    break

            dp[i] = min_step
        
        return dp[n - 1]
