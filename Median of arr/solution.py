class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
    
        if n % 2 != 0:
            return arr[n // 2]
        else:
            mid1 = arr[(n // 2) - 1]
            mid2 = arr[n // 2]
            return (mid1 + mid2) / 2
