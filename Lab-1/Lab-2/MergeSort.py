# Applying merge sort algorithm Sorting the array element .
n=int(input("Enter the size of array:"))
array=[]
for i in range(n):
  array.append(int(input(f"Enter Element {i}:")))

print(f"The Unsorting data:{array}")


def merge_sort(values):
  if len(values) <= 1:
    return values

  middle = len(values) // 2
  left = merge_sort(values[:middle])
  right = merge_sort(values[middle:])
  sorted_values = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      sorted_values.append(left[i])
      i += 1
    else:
      sorted_values.append(right[j])
      j += 1

  sorted_values.extend(left[i:])
  sorted_values.extend(right[j:])
  return sorted_values


array = merge_sort(array)
print(f"The Sorted data Using MergeSort:{array}")

