class Solution:
        
    def minSwap (self,arr, k) : 
        #Complete the function  
        n = len(arr)
        count = 0
        for x in arr:
            if x <= k:
                count += 1

        if count <= 1:
            return 0

        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1

        ans = bad
        for i in range(n - count):
            if arr[i] > k:
                bad -= 1
            if arr[i + count] > k:
                bad += 1
            if bad < ans:
                ans = bad

        return ans
