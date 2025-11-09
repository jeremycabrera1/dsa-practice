# Given an array and a number k, find the maximum sum of any contiguous subarray of size k.

# Example:

arr = [4, 2, 1, 7, 8, 1, 2, 8, 10]
k = 3


# We want to find which 3 consecutive numbers give the highest total.


def max_sum_subarray(arr:list, k:int) -> int:
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(max_sum_subarray(arr, k))