# Given an array of integers.

# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# my solution

def count_positives_sum_negatives(arr):
    plus = len([i for i in arr if i > 0])
    minus = sum([i for i in arr if i < 0])
    if arr == []:
        return []
    else: return [plus, minus]