class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in counts.items():
            buckets[freq].append(char)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for char in buckets[i]:
                res.append(char * i)

        return "".join(res)

s = "tree"
obj = Solution()
print(obj.frequencySort(s))
