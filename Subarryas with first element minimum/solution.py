class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        nse = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                nse[stack.pop()] = i
            stack.append(i)
            
        total_count = 0
        for i in range(n):
            total_count += (nse[i] - i)
            
        return total_count
