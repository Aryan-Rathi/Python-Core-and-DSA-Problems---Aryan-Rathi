import heapq

class Solution:
    def minOperations(self, arr):
        n = len(arr)
        initial_sum = sum(arr)
        target = initial_sum / 2.0
        current_sum = float(initial_sum)
        
        max_heap = [-float(x) for x in arr]
        heapq.heapify(max_heap)
        
        operations = 0
        while current_sum > target:
            max_val = -heapq.heappop(max_heap)
            reduction = max_val / 2.0
            current_sum -= reduction
            
            heapq.heappush(max_heap, -reduction)
            operations += 1
            
        return operations
