class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        max_so_far = arr[0]
        curr_sum = arr[0]
        for i in range(1, len(arr)):
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_so_far = max(max_so_far, curr_sum)
            
        return max_so_far
