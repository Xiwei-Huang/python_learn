# cp功能
import sys
if len(sys.argv) != 3:
    print('usage: cp source_file target_file')
    sys.exit()

source_file,target_file=sys.argv[1],sys.argv[2]
with open(source_file,'rb') as read_f,open(target_file,'wb') as write_f:
    for line in read_f:
        write_f.write(line)

# 练习：基于seek实现tail -f功能
import time
with open('test.txt','rb') as f:
    f.seek(0,2)
    while True:
        line=f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)

#%% 将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘
import os

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    data=read_f.read() #全部读入内存,如果文件很大,会很卡
    data=data.replace('albert','NB') #在内存中完成修改

    write_f.write(data) #一次性写入新文件

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')

# 将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件
import os

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('albert','NB')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')

# 练习
'''
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
2. 修改文件内容，把文件中的mac都替换成linux
'''

# 写入
f = open('a.txt','w',encoding='utf-8')
f.write('apple 10 3\ntesla 100000 1\nmac 3000 2\nlenovo 30000 3\nchicken 10 3\n')
f.close()

# 修改
import os
with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('mac','linux')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')

