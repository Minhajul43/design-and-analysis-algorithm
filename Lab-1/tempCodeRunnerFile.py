n=int(input("Enter the size of array:"))
numbers=[]
for i in range(n):
	numbers.append(int(input(f"Enter Element {i}:")))
print(f"Unsorted given number:{numbers}")
target=int(input(f"Enter Search value:"))