def reverse1(L: list) -> list:
   if L == []: return []
   return reverse1(L[1:]) + [L[0]]

def reverse_c(L: list) -> None:
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
