print('WELCOME TO QUEUE')
l=[]
while True:
    print('please select the operation you want to use\n1.enqueue 2.dequeue 3.size of stack 4.emptiness 5.exit')
    a=input()
    a=int(a)
    b=len(l)
    if a==1:
        print('ENTER THE NUMBER YOU WANT TO ADD')
        element=input()
        l.append(element)
        print(l)
    elif a==2:
        if b==0:
            print('cannot remove element because queue is empty')
        else:
            print('remove the number')
            l.pop(0)
            print(l)
    elif a==3:
        print('the size of queue is')
        print(len(l))
        print(l)
    elif a==4:
        if b==0:
            print('queue is empty')
        else:
            print('queue is not empty')
    elif a==5:
        print('**************************You have exited the queue**************************')
        break;
    elif a>=6:
        print('We have only five operations\nPlease choose the above options')
    
    
