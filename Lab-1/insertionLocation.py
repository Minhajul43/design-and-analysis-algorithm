# insertion element into location that's given from the user.

n=int(input("Enter the size of array:"))
array=[]
for i in range(0,n):
  array.append(int(input(f"Element {i} is :")))
print(array)

digit=int(input("Enter the element that's you insert:"))
location=int(input("Enter the location:"))

array.append(0)
for i in range(n, location, -1):
  array[i]=array[i-1]
array[location]=digit
# array.insert(location,digit)

print(array)