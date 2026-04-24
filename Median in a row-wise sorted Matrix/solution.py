from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = mat[0][0]
        high = mat[0][0]
        for i in range(n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][m-1])
            
        median_pos = (n * m) // 2
        
        while low <= high:
            mid = (low + high) // 2
            count = 0
            
            for i in range(n):
                count += bisect_right(mat[i], mid)
            
            if count <= median_pos:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
