ch=int(raw_input())
b=0
for i in range(2,ch//3):
    if(ch%i==0):
        b=b+1
if(b<=0):
    print("yes")
else:
    print("no")
