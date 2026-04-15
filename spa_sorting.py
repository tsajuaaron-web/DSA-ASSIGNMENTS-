import time
import random
import sys

# Increase recursion depth for Quick Sort on sorted datasets
sys.setrecursionlimit(20000)

# --- Task 1: Sorting Algorithms ---

def insertion_sort(arr):
    """Sorts the list in non-decreasing order (Stable, In-place)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Sorts using Divide & Conquer (Stable, Out-of-place)."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for Merge Sort."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, low, high):
    """Sorts using partitioning (Usually Unstable, In-place)."""
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    """Lomuto partition scheme using the last element as pivot."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- Task 2: Utility & Experiments ---

def measure_time(sort_func, arr, is_quick=False):
    """Measures execution time in milliseconds."""
    arr_copy = arr.copy()
    start = time.time()
    if is_quick:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)
    end = time.time()
    return (end - start) * 1000  # Convert to ms

def generate_datasets():
    sizes = [1000, 5000, 10000]
    data_types = ['Random', 'Sorted', 'Reverse-Sorted']
    datasets = {}
    
    for size in sizes:
        datasets[(size, 'Random')] = [random.randint(1, 100000) for _ in range(size)]
        datasets[(size, 'Sorted')] = list(range(size))
        datasets[(size, 'Reverse-Sorted')] = list(range(size, 0, -1))
    return datasets

def main():
    # Correctness Check
    test_arr = [5, 2, 9, 1, 5, 6]
    print(f"Correctness Check: Input {test_arr}")
    print(f"Insertion Sort: {insertion_sort(test_arr.copy())}")
    print(f"Merge Sort:     {merge_sort(test_arr.copy())}")
    quick_test = test_arr.copy()
    quick_sort(quick_test, 0, len(quick_test)-1)
    print(f"Quick Sort:     {quick_test}")
    print("-" * 50)

    # Experiments
    datasets = generate_datasets()
    print(f"{'Size':<10} | {'Type':<15} | {'Insertion (ms)':<15} | {'Merge (ms)':<15} | {'Quick (ms)':<15}")
    print("-" * 80)
    
    for size in [1000, 5000, 10000]:
        for d_type in ['Random', 'Sorted', 'Reverse-Sorted']:
            data = datasets[(size, d_type)]
            
            t_ins = measure_time(insertion_sort, data)
            t_mrg = measure_time(merge_sort, data)
            t_qck = measure_time(quick_sort, data, is_quick=True)
            
            print(f"{size:<10} | {d_type:<15} | {t_ins:<15.2f} | {t_mrg:<15.2f} | {t_qck:<15.2f}")

if __name__ == "__main__":
    main()