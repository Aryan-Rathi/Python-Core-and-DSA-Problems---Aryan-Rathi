class Solution:
	def minJumps(self, arr):
	    # code here
	    n = len(arr)
	    crr_end = 0
	    far = 0
	    jump = 0
	    if n<=1:
	        return 0
	    if arr[0]==0:
	        return -1
	    for i in range(n-1):
	        far = max(far, i + arr[i])
	        if i == crr_end:
	            jump += 1
	            crr_end=far
	            if crr_end>=n-1:
	                return jump
	        if i>=far:
	            return -1
	    return -1
