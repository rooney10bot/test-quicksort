"""
QuickSort Algorithm
A divide-and-conquer algorithm that selects a 'pivot' element and partitions the array.
Time Complexity: O(n log n) average, O(n²) worst
Space Complexity: O(log n)
"""

def quicksort(arr):
    """
    Sort an array using quicksort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    In-place quicksort using partition scheme.
    More memory efficient than the basic version.

    Args:
        arr: List of elements to sort
        low: Starting index
        high: Ending index
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    Lomuto partition scheme.

    Args:
        arr: List to partition
        low: Starting index
        high: Ending index

    Returns:
        Index of the pivot
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Test the implementation
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]

    print(f"Original array: {test_array}")
    print(f"Sorted array (functional): {quicksort(test_array.copy())}")

    # Test in-place version
    test_array_copy = test_array.copy()
    quicksort_inplace(test_array_copy)
    print(f"Sorted array (in-place): {test_array_copy}")

    # Test with edge cases
    empty_array = []
    single_element = [42]
    already_sorted = [1, 2, 3, 4, 5]
    reverse_sorted = [5, 4, 3, 2, 1]

    print("\nEdge case tests:")
    print(f"Empty: {quicksort(empty_array)}")
    print(f"Single: {quicksort(single_element)}")
    print(f"Already sorted: {quicksort(already_sorted)}")
    print(f"Reverse sorted: {quicksort(reverse_sorted)}")
