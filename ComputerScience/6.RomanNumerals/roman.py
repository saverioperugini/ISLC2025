def int_to_Roman(num):
   val = [
       1000, 900, 500, 400,
       100, 90, 50, 40,
       10, 9, 5, 4,
       1
       ]
   sym = [
       "M", "CM", "D", "CD",
       "C", "XC", "L", "XL",
       "X", "IX", "V", "IV",
       "I"
       ]
   roman_num = ''
   i = 0
   while  num > 0:
      for _ in range(num // val[i]):
         roman_num += sym[i]
         num -= val[i]
      i += 1
   return roman_num

n = int(input("\nEnter a year as an integer: "))

print("\nThe year", n, "formatted as a Roman numeral is:", int_to_Roman(n), '\n')
