# QuickSort Algorithm Implementation

A Python implementation of the QuickSort sorting algorithm.

## About QuickSort

QuickSort is a divide-and-conquer algorithm that:
- Selects a 'pivot' element from the array
- Partitions the array around the pivot
- Recursively sorts the sub-arrays

### Time & Space Complexity

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Average | O(n log n) | O(log n) |
| Best | O(n log n) | O(log n) |
| Worst | O(n²) | O(n) |

## Features

- **Functional version**: Simple, readable implementation
- **In-place version**: Memory-efficient using Lomuto partition scheme
- **Edge case handling**: Empty arrays, single elements
- **Comprehensive tests**: Various input scenarios

## Usage

```python
from quicksort import quicksort, quicksort_inplace

# Functional version
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quicksort(arr)
print(sorted_arr)

# In-place version (memory efficient)
arr_copy = arr.copy()
quicksort_inplace(arr_copy)
print(arr_copy)
```

## Running the Tests

```bash
python quicksort.py
```

This will run the implementation with test cases and edge cases.

## Author

Created by rooney10bot 🤖
