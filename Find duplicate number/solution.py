class Solution(object):
    def findDuplicate(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]==nums[j]:
                     return nums[i]
                else:
                    continue
        return 0
