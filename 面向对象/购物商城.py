'''
需求:
1.用户名和密码存放于文件中，格式为：Albert|Albert123                                               1.字典存放     ！！！进阶：2.写入文件  读取文件（读格式还不会）
2.启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，                  OK
3.超过三次则退出程序,并将用户名添加到黑名单，再次启动程序登陆该用户名，提示用户禁止登陆            使用lock黑名单，在重复三次之后将名单添加到lock
4.允许用户根据商品编号购买商品                                                                     一个key有多值
5.用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒                                         
6.可随时退出，退出时，打印已购买商品和余额

未实现功能：
1.商品编号
2.黑名单
3.买多个/多种商品

问题：
针对3：再一次登录时如何保留“黑名单”里面的人

总结：
写循环的时候陷在多层循环里了，用了一个tag=False也没有用，
参考：https://blog.csdn.net/feng98ren/article/details/79693702
https://www.aliyun.com/jiaocheng/505279.html
法一：封装函数：return（本章不使用函数，第二章再用）
法二：使用flag+break（本文）
法三：while--tag
法四：自定义异常 
'''

# 商品三级清单
menu = {
    '食品':{
        '生鲜':{
            '肉类':{
                '鱼':20,'小龙虾':40,'鸡肉':15,'牛肉':20,'禽蛋':5,
            },
            '果蔬':{
                '苹果':9.9,'香蕉':8,'黄瓜':6,'卷心菜':4,
            },
            '速食':{
                '饺子':10,'汤圆':7,
            },
        },
        '休闲零食':{
            '零食礼包':{
                '乐事':10,'薯愿':8,'小饼干':5,
            },
            '网红零食':{'脏脏包':40},
            '进口零食':{'礼包':100,'德芙巧克力':10},
        },
        '奶品水饮':{'酸奶':3},
        '粮油副食':{'酱油':7},
    },
    '日用品':{
        '厨卫':{
            "洗衣液":30
        },
        '清洁':{
            '纸巾':5
        },
    },
    '美妆':{'面膜':80},
}

# 用户字典与黑名单
info = {'Albert':123 ,'Tom':456, 'Jack':789}

# 写入
f = open('info.txt','w',encoding='utf-8')
f.write('Albert|123\nTom|456\nJack|789\n')
f.close()

lock = {}
time = 0
tag = False            #用来进入打印列表环节
tag1 = False           #用来进入结账环节
flag = False           #用来跳出多重循环

while 1:
    while time<3:
        name=input('用户名: ')
        password=int(input('密码: '))
        if name in lock.keys():
            print('该用户已经被禁止')
        else:
            if name in info.keys():                 #判断名字在字典里
                if info[name] != password:          #输入名字给info赋值
                    print('错误')
                    time += 1
                    print('你还有{}次机会'.format(3 - time))
                    continue
                else:
                    print('登录成功')
                    time = 0
                    flag =  True
                    tag = True
                    break
            else:
                print('用户未注册')
        if flag == True:
            break
    if flag == True:
        break
    else:
        lock[name] = name
        time = 0
        print('登录异常,该用户名已被锁定')
        break

while tag:
    income =float(input('你的工资是;'))
    print('欢迎，下面是商品列表，在购物过程中按b返回商品列表上层，选购完毕则按p结账')
    for key, value in menu.items():
        print(key, value)

    menu1 = menu
    for key in menu1: # 打印第一层
        print(key)

    choice1=input('第一层>>: ').strip() # 选择第一层

    if choice1 == 'b': # 输入b，则返回上一级
        break
    if choice1 == 'p': # 输入p，则退出商品结账
        tag = False
        continue
    if choice1 not in menu1: # 输入内容不在menu1内，则继续输入
        print('请重新输入：')
        continue

    while tag:
        menu_2=menu1[choice1] # 拿到choice1对应的一层字典
        for key in menu_2:
            print(key)

        choice2 = input('第二层>>: ').strip()

        if choice2 == 'b':
            break
        if choice2 == 'p':
            tag = False
            continue
        if choice2 not in menu_2:
            print('请重新输入：')
            continue

        while tag:
            menu_3=menu_2[choice2]
            for key in menu_3:
                print(key)

            choice3 = input('第三层>>: ').strip()
            if choice3 == 'b':
                break
            if choice3 == 'p':
                tag = False
                continue
            if choice3 not in menu_3:
                print('请重新输入：')
                continue

            while tag:
                menu_4=menu_3[choice3]
                for key in menu_4:
                    print(key)

                choice4 = input('第四层>>: ').strip()
                if choice4 == 'b':
                    break
                if choice4 == 'q':
                    tag = False
                    continue
                if choice4 not in menu_4:
                    print('请重新输入：')
                    continue

if tag == False:
    print('您购买了{},一共{}元'.format(choice4,sum))