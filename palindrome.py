ch=int(raw_input())
temp=ch
rev=0
while(ch>0):
    dig=ch%10
    rev=rev*10+dig
    ch=ch//10
if(temp==rev):
    print("yes")
else:
    print("no")
