class Solution(object):
    def combinationSum2(self, arr, target):
        arr.sort()
        ans = []

        def backtrack(index, target, ds):
            if target == 0:
                ans.append(list(ds))
                return

            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i-1]:
                    continue

                if arr[i] > target:
                    break

                ds.append(arr[i])

                backtrack(i + 1, target - arr[i], ds)
                ds.pop()

        backtrack(0, target, [])
        return ans
            
        
