def reverse_i(L: list) -> list:
   size = len(L)
   i = 1
   newlist = []

   while i <= size:
      newlist += [(L[size-i])]
      i += 1

   return newlist

# another iterative version of reverse
# Note: reverse_i2 is NOT a function.
# It has no return value # and it modifies L in place.
# That is, L appears on the left-hand side
# of an assignment statement.
def reverse_i2(L: list) -> None:
   size = len(L)

   for i in range(int(size/2)):
      temp = L[i]
      L[i] = L[size-(i+1)]
      L[size-(i+1)] = temp

list1 = []
list2 = [1,4,5,2]
list3 = ["night","and","day"]
list4 = ["A","very","short","sentence","."]
list5 = [[1,2,3],[4,5,6],[7,8,9]]

print(reverse_i(list1))
print(reverse_i(list2))
print(reverse_i(list3))
print(reverse_i(list4))
print(reverse_i(list5))

reverse_i2(list1)
reverse_i2(list2)
reverse_i2(list3)
reverse_i2(list4)
reverse_i2(list5)

print (list1)
print (list2)
print (list3)
print (list4)
print (list5)
