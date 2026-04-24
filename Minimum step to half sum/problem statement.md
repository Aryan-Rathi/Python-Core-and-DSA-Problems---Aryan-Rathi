Given an array arr[], find the minimum number of operations required to make the sum of its elements less than or equal to half of the original sum. In one operation, you may replace any element with half of its value (with floating-point precision).

Examples:

Input: arr[] = [8, 6, 2]

Output: 3

Explanation: Initial sum = (8 + 6 + 2) = 16, half = 8

Halve 8 → arr[] = [4, 6, 2], sum = 12 (still 12 > 8)

Halve 6 → arr[] = [4, 3, 2], sum = 9 (still 9 > 8)

Halve 2 → arr[] = [4, 3, 1], sum = 8. 
