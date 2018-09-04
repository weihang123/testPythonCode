def add(a,b):
    c=a+b
    return c;
d=add(1,2)
print(d)
print('-------------')

def add(a,b):
    c=a+b
    print(c)
add(1,2)


#不定长参数
#参数带*号，一个*输出结果为元组

def test01(str,*tup):
    print(str)
    print(tup)
    return

test01('canshu',11,12)

#参数带**，两个*表示字典
def test02(str,**dict):
    print(str)
    for i in dict:
        print(dict[i])
    return

test02(1,a=2,b=3,c=4)

def test03(a):
    print(a)
test03(1)



