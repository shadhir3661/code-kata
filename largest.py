inputvalue=raw_input()
a,b,c=inputvalue.split(" ")
if (a>b) and (a>c):
   print(a)
elif (b>a) and (b>c):
   print(b)
else:
   print(c)
