class Solution:    
    def findUnion(self, a, b):
        # code here
        return sorted(list(set(a+b)))  
