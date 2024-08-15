#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def merge_count_split_inv(arr, temp_arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = 0

    inv_count += merge_count_split_inv(arr, temp_arr, left, mid)
    inv_count += merge_count_split_inv(arr, temp_arr, mid + 1, right)
    inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    
    j = mid + 1 
    k = left    
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def insertionSort(arr):
    temp_arr = [0] * len(arr)
    return merge_count_split_inv(arr, temp_arr, 0, len(arr) - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
