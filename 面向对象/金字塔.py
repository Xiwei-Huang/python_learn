a=5
for n in range(1,a+1):
    for i in range(a-n):
        print(' ',end='') #打印多个空格
    for j in range(2*n-1):
        print('*',end='') #打印多个*
    print()

