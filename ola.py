print('welcome to ola')
place=["tambaram","adyar","ambatur"]
distance=[35,30,50]
print("please select destination\n1.tambaram,2.adayar,3.ambathur")
dest=int(input())
if dest==1:
    kms=distance[0]
elif dest==2:
    kms=distance[1]
elif dest==3:
    kms=distance[2]
print('please mention type of cab\n 1.nano,2.micro,3.mini,4.prime')
nano=5
micro=8
mini=10
prime=15
choice=int(input())
if choice==1:
    b=kms*nano
elif choice==2:
    b=kms*micro
elif choice==3:
    b=kms*mini
elif choice==4:
    b=kms*prime
print("the amount for your trip is",b)



