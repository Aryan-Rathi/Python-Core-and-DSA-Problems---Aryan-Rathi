class Solution:
    def minMen(self, arr):
        n = len(arr)
        if n == 0: return -1
        
        max_reach = [-1] * n
        for i in range(n):
            if arr[i] != -1:
                start = max(0, i - arr[i])
                end = min(n - 1, i + arr[i])
                max_reach[start] = max(max_reach[start], end)
        
        jumps = 0
        current_end = -1
        farthest = -1
        
        for i in range(n):
            if max_reach[i] != -1:
                farthest = max(farthest, max_reach[i])
            
            if i > farthest:
                return -1
                
            if i > current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    return jumps
                    
        return jumps if current_end >= n - 1 else -1
