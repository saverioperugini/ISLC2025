def reverse1(L: list) -> list:
   if L == []: return []
   return reverse1(L[1:]) + [L[0]]

def reverse1(L: list) -> list:
   if L == [] or L == "": return L
   #else:
   #   return reverse1(L[1:]) + [L[0]]
   elif type(L) == str: return reverse1(L[1:]) + L[0]
   elif type(L) == list: return reverse1(L[1:]) + [L[0]]

def ispalindrome(s: str) -> bool:
   return reverse1(s) == s

list1 = []
list2 = [1,4,5,2]
list3 = ["night","and","day"]
list4 = ["A","very","short","sentence","."]
list5 = [[1,2,3],[4,5,6],[7,8,9]]

print (list1)
print (list2)
print (list3) 
print (list4)
print (list5)
         
print('')

print(reverse1([]))
print(reverse1([1,4,5,2]))
print(reverse1(["night","and","day"]))
print(reverse1(["A","very","short","sentence","."]))
print(reverse1([[1,2,3],[4,5,6],[7,8,9]]))
