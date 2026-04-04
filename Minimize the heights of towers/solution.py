class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        arr.sort()
        ans = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        for i in range(n - 1):
            if arr[i+1] < k:
                continue
            curr_min = min(smallest, arr[i+1] - k)
            curr_max = max(largest, arr[i] + k)
            ans = min(ans, curr_max - curr_min)
        return ans
