# Create a array and print this . Get array size from user and create a array.

n=int(input("Enter the size of array:"))
array=[]
for i in range(0,n):
  array.append(int(input(f"Element {i} is:")))

print(array)  
