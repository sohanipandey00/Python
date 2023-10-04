a=int(input("Enter the no. of rows:"))
for i in range(a):
    for j in range(i):
        print('',end='')
    for j in range(2*(a-i)-1):
        print(j+1,end='')
    print("")