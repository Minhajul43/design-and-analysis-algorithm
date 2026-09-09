# Binary search works on a sorted list.


def binary_search(numbers, target):
	"""Return the index of target, or -1 if it is not found."""
	left, right = 0, len(numbers) - 1

	while left <= right:
		middle = (left + right) // 2

		if numbers[middle] == target:
			return middle
		if numbers[middle] < target:
			left = middle + 1
		else:
			right = middle - 1

	return -1


# Customize these values as needed. Keep the list sorted.
numbers = [3, 7, 12, 18, 25, 31, 42]
target = 25

result = binary_search(numbers, target)
if result == -1:
	print(f"{target} was not found")
else:
	print(f"{target} found at index {result}")

