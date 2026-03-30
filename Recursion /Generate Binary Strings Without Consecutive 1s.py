class Solution:
    def generateBinaryStrings(self, n):
        # Your code goes here
        def generate(curr):
            if len(curr) == n:
                return [curr]

            res = []
            res.extend(generate(curr  + '0'))

            if not curr or curr[-1] != '1':
                res.extend(generate(curr  + '1'))

            return res
        return generate("")
