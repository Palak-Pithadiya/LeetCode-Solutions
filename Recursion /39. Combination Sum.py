class Solution(object):
    def combinationSum(self, arr, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def findCombination(index, current_target, ds):
            if current_target == 0:
                ans.append(ds)
                return

            if index == len(arr) or current_target < 0:
                return

            # CHOICE 1: Pick (Multiple)
            findCombination(index, current_target - arr[index], ds + [arr[index]])

            # CHOICE 2: Exclude
            findCombination(index + 1, current_target, ds)

        findCombination(0, target, [])
        return ans
