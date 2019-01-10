# 关系运算
pythons={'albert','孙悟空','周星驰','朱茵','林志玲'}
ais={'猪八戒','郭德纲','林忆莲','周星驰'}
print(pythons & ais)
print(pythons | ais)
print(pythons - ais)
print(pythons ^ ais)

# 去重
l1=['a','b',1,'a','a']
l2=[
    {'name':'albert','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'albert','age':20,'sex':'female'},
    {'name':'albert','age':18,'sex':'male'},
    {'name':'albert','age':18,'sex':'male'},
]

print(set(l1))

l3=[]
s=set()
for i in l1:
    if i not in s:
        s.add(i)
        l3.append(i)
print(l3)

