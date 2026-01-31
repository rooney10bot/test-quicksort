"""
Unit tests for QuickSort algorithm implementation
"""

import unittest
import random
from quicksort import quicksort, quicksort_inplace, partition


class TestQuickSortFunctional(unittest.TestCase):
    """Test functional quicksort implementation"""

    def test_empty_array(self):
        """Test sorting empty array"""
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        """Test sorting single element"""
        self.assertEqual(quicksort([42]), [42])

    def test_already_sorted(self):
        """Test sorting already sorted array"""
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test sorting reverse sorted array"""
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_array(self):
        """Test sorting random array"""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        expected = sorted(arr)
        self.assertEqual(quicksort(arr), expected)

    def test_duplicates(self):
        """Test sorting array with duplicates"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = sorted(arr)
        self.assertEqual(quicksort(arr), expected)

    def test_negative_numbers(self):
        """Test sorting array with negative numbers"""
        arr = [-5, 3, -1, 0, 2, -3, 4]
        expected = sorted(arr)
        self.assertEqual(quicksort(arr), expected)

    def test_floats(self):
        """Test sorting array with floats"""
        arr = [3.14, 1.59, 2.65, 0.5, 4.2]
        expected = sorted(arr)
        self.assertEqual(quicksort(arr), expected)

    def test_large_array(self):
        """Test sorting large array (1000 elements)"""
        arr = [random.randint(0, 10000) for _ in range(1000)]
        expected = sorted(arr)
        self.assertEqual(quicksort(arr), expected)


class TestQuickSortInPlace(unittest.TestCase):
    """Test in-place quicksort implementation"""

    def test_empty_array(self):
        """Test sorting empty array"""
        arr = []
        quicksort_inplace(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        """Test sorting single element"""
        arr = [42]
        quicksort_inplace(arr)
        self.assertEqual(arr, [42])

    def test_already_sorted(self):
        """Test sorting already sorted array"""
        arr = [1, 2, 3, 4, 5]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test sorting reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        quicksort_inplace(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        """Test sorting random array"""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_duplicates(self):
        """Test sorting array with duplicates"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_negative_numbers(self):
        """Test sorting array with negative numbers"""
        arr = [-5, 3, -1, 0, 2, -3, 4]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)

    def test_large_array(self):
        """Test sorting large array (1000 elements)"""
        arr = [random.randint(0, 10000) for _ in range(1000)]
        expected = sorted(arr)
        quicksort_inplace(arr)
        self.assertEqual(arr, expected)


class TestPartition(unittest.TestCase):
    """Test partition function"""

    def test_partition_basic(self):
        """Test basic partition"""
        arr = [10, 80, 30, 90, 40, 50, 70]
        pivot_index = partition(arr, 0, len(arr) - 1)
        # After partition, pivot should be in correct position
        # All elements before pivot should be <= pivot
        # All elements after pivot should be > pivot
        pivot = arr[pivot_index]
        for i in range(pivot_index):
            self.assertLessEqual(arr[i], pivot)
        for i in range(pivot_index + 1, len(arr)):
            self.assertGreater(arr[i], pivot)

    def test_partition_with_duplicates(self):
        """Test partition with duplicate values"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        pivot_index = partition(arr, 0, len(arr) - 1)
        pivot = arr[pivot_index]
        for i in range(pivot_index):
            self.assertLessEqual(arr[i], pivot)
        for i in range(pivot_index + 1, len(arr)):
            self.assertGreater(arr[i], pivot)


class TestConsistency(unittest.TestCase):
    """Test consistency between functional and in-place versions"""

    def test_consistency(self):
        """Test both versions produce same result"""
        test_cases = [
            [],
            [42],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [64, 34, 25, 12, 22, 11, 90],
            [3, 1, 4, 1, 5, 9, 2, 6, 5],
            [-5, 3, -1, 0, 2, -3, 4],
            [random.randint(0, 1000) for _ in range(100)],
        ]

        for arr in test_cases:
            arr1 = arr.copy()
            arr2 = arr.copy()
            result1 = quicksort(arr1)
            quicksort_inplace(arr2)
            result2 = arr2

            self.assertEqual(result1, result2, f"Mismatch for array: {arr}")
            self.assertEqual(result1, sorted(arr), f"Result not sorted correctly: {arr}")


def run_tests():
    """Run all tests and display results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestQuickSortFunctional))
    suite.addTests(loader.loadTestsFromTestCase(TestQuickSortInPlace))
    suite.addTests(loader.loadTestsFromTestCase(TestPartition))
    suite.addTests(loader.loadTestsFromTestCase(TestConsistency))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print("="*70)

    return result.wasSuccessful()


if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)
