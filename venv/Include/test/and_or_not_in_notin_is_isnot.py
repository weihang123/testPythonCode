
#and、or、not
a =10

b =10

if(a and b):
    print("1: 变量a 和 b 都为true")
else:
    print("1: 变量a 和 b 有一个不为true")

if(a or b):
    print("2: 变量a 和 b 有一个为true，那么就执行if语句表达式就true")

else:
    print("2: 变量a 和 b 都为false，那么就执行if语句表达式就false")

if(not (a and b)):
    print("aaaaaa")
else:
    print("ddddd")


#in、not in

a =10
b =20
list =[1,2,3,4,5]

if(a in list):
    print("a在list列表中存在数据")
else:
    print("a在list列表中不存在")
    list.append(20)
    list.remove(list[1])
    print(list)
    print(list[0:2])

if(b not in list):
    print("b在列表中不存在返回true")
else:
    print("b在列表中存在为true返回结果为false")

#is、not is

a,b =10,10
if(a is b):
    print("a跟b引用的是同一个对象")




