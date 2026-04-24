You are given an integer array arr[ ]. Your task is to count the number of subarrays where the first element is the minimum element of that subarray.

Note: A subarray is valid if its first element is not greater than any other element in that subarray.

Examples:

Input: arr[] = [1, 2, 1]

Output: 5

Explanation:

All possible subarrays are:

[1], [1, 2], [1, 2, 1], [2], [2, 1], [1]

Valid subarrays are:

[1], [1, 2], [1, 2, 1], [2], [1] -> total 5
