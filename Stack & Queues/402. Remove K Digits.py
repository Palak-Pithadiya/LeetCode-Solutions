class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        final_stack = stack[:-k] if k > 0 else stack

        res = "".join(final_stack).lstrip('0')
        
        return res if res else '0'
