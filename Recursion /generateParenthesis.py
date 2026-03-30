class Solution(object):
    def backTrack(self, curr, open, close, n, res):
        if len(curr) == 2 * n:
            res.append(curr)
            return res

        if open < n:
            self.backTrack(curr + '(', open + 1, close, n, res)
        if close < open:
            self.backTrack(curr + ')', open, close + 1, n, res)

    def generateParenthesis(self, n):
        res = []
        self.backTrack("", 0, 0, n, res)
        return res
        
