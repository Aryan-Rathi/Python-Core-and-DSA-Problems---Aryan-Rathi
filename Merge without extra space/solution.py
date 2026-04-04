class Solution:
    def mergeArrays(self, a, b):
        # code here
        n=len(a)
        m=len(b)
        a.extend(b)
        a.sort()
        b[:]=a[n:]
        a[:]=a[:n]
        return a,b
