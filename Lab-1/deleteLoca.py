# delete element from specific location from the array

n=int(input("Enter the size of arrayList:"))
array=[]
for i in range(0,n):
  array.append(int(input(f"Enter element {i}:")))

print(array)
delate=int(input("Enter delate element index:"))

array.pop(delate)
print(array)