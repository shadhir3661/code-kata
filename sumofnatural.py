a =int(raw_input())
if a< 0:
   print("Enter a positive number")
else:
   sum = 0
   while(a> 0):
       sum += a
       a -= 1
   print(sum)
