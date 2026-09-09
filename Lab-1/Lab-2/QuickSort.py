# Quick Sort with custom logic

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


n = int(input("Enter the size of array: "))
array = []

for i in range(n):
    array.append(int(input(f"Enter Element {i}: ")))

print(f"The unsorted data: {array}")

sorted_array = quick_sort(array)
print(f"The sorted data Using QuickSort: {sorted_array}")


