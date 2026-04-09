import math
class Solution:
    def factorial(self, n):
        res_num = math.factorial(n)
        res_str = str(res_num)
        return [int(digit) for digit in res_str]
