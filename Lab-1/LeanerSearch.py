# search element from the created array

n=int(input("Enter the size of array:"))
array=[]
for i in range(n):
  array.append(int(input(f"Enter element {i}:")))

print(array)
value=int(input("Enter the value that's you search:"))

found=False
for i in range(n):
 if array[i]==value:
  print(f"Your Searching element is {i}")
  found=True
  break
 if not found:
  print(f"There are no element of {value}")
