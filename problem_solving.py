#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Descriotion of the problem:
# let the value of a 0-indexed array be defined as the square of the sum of 
# even-indexed elements minus the sum of odd-indexed elements. For example,
# if arr = [2,-1,-4,5] the square of the sum of even-indexed elements(2, -4)
# minus the sum of odd-indexed elements(-1, 5) is ((2-4)-(-1+5) )^2 = (-2-4)^2 = 36.
# Given an array of integers, what is the maximum subarrays value among all of its subarrays?
# lets say arr = [-1,-4,2], in this case subarray [-4,2] has the maximum subarray value of 36. so the answer is 36.
# 5 1 -1 1 -1 1
# 25
def maxSubarrayValue(arr):
    # Write your code here
    subarrays = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            subarrays.append(arr[i:j])
    max_value = 0
    for subarray in subarrays:
        even_sum = 0
        odd_sum = 0
        for i in range(len(subarray)):
            if i % 2 == 0:
                even_sum += subarray[i]
            else:
                odd_sum += subarray[i]
        value = (even_sum - odd_sum) ** 2
        if value > max_value:
            max_value = value
    return max_value

def maxSubarrayValue1(arr):
    # Write your code here
    max_value = 0
    for i in range(len(arr)):
        even_sum = 0
        odd_sum = 0
        for j in range(i, len(arr)):
            if j % 2 == 0:
                even_sum += arr[j]
            else:
                odd_sum += arr[j]
            value = (even_sum - odd_sum) ** 2
            if value > max_value:
                max_value = value
    return max_value

def maxSubarrayValue2(arr):
    # more efficient solution
    # Write your code here
    return max([((sum(arr[i:j]) - sum(arr[i+1:j:2])) ** 2) for i in range(len(arr)) for j in range(i+1, len(arr)+1)])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxSubarrayValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
