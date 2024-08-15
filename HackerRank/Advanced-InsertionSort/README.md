# Advanced-InsertionSort

## Problem Statement

The problem involves a modified version of the insertion sort algorithm. Given an array of integers, the task is to count the number of shifts required to sort the array using the insertion sort technique.

**Link to Problem:**  
[Insertion Sort Advanced Analysis on HackerRank](https://www.hackerrank.com/challenges/insertion-sort/problem?isFullScreen=true)

## Initial Approach

The initial approach involved directly implementing the insertion sort algorithm. This method works by iterating through the array and for each element, counting the number of shifts required to place it in the correct position within the sorted portion of the array. The total number of shifts gives the desired result.


## Code

```python
def insertionSort(arr):
    shift_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shift_count += 1
            j -= 1
        arr[j + 1] = key
    return shift_count

# Example usage:
n = int(input())
arr = list(map(int, input().split()))
print(insertionSort(arr))
```


### Limitations

While this approach works well for smaller arrays, it has a time complexity of \(O(n^2)\). This quadratic time complexity becomes a bottleneck for large datasets, leading to a "Time limit exceeded" error.

## Optimized Approach

To overcome the limitations of the initial approach, a more efficient algorithm was implemented using a modified merge sort. The key idea is to count the number of inversions in the array during the merge process. An inversion is a situation where a larger number precedes a smaller number in the array, and counting these gives the number of shifts needed for sorting.

The merge sort algorithm has a time complexity of \(O(n \log n)\), making it suitable for handling larger datasets within the time constraints.

### Implementation

The optimized solution involves recursively splitting the array and counting inversions while merging the sorted halves. This approach efficiently counts the required shifts, significantly reducing the execution time.

For the detailed code implementation, please refer to the `solution.py` file in this directory.

---

Happy Coding!
