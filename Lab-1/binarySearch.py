# Binary search 

def binary_search(numbers, target):
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


n=int(input("Enter the size of array:"))
numbers=[]
for i in range(n):
	numbers.append(int(input(f"Enter Element {i}:")))

print(f"Unsorted given number:{numbers}")
target=int(input(f"Enter Search value:"))

result = binary_search(numbers, target)
if result == -1:
	print(f"{target} was not found")
else:
	print(f"{target} found at index {result}")

