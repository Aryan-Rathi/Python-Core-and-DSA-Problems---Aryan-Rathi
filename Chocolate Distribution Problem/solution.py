class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        if m == 0 or n == 0:
            return 0
        if n < m:
            return -1
        arr.sort()
        return min(arr[i + m - 1] - arr[i] for i in range(n - m + 1))
