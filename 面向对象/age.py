print("猜测年龄")
age = 18
tag=True
while tag:
    for i in range(3):
        a = int(input("输入年龄："))
        if a < age:
            print("小了")
        elif a > age:
            print("大了")
        else:
            print("猜对了")
            break
    print("是否继续猜？")
    b = int(input("是就输入1,否就输入0："))
    if b == 1:
        continue
    else:
        tag = False
'''
1. 一开始的错误：if b =='y'
2. 可以设置count为3，之后用户输入y则清零
3. if b =='y'里面用pass？？？？？

'''




