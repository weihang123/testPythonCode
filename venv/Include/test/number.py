#六个数据类型之---number(数字)
#number(数字包括)：int（整型）、float(浮点型)、bool（布尔）、complex(复数)

#int
a =100
#打印出a的变量类型
print(type(a))

#float
b = 1.23
#打印出b的变量类型
print(type(b))

#bool
c = False
#打印出c的变量类型
print(type(c))

#complex
d = 12j+1
#打印出d的变量类型
print(type(d))

#python可以同时为不同的变量赋值

q,w,e = 1,1.5,True
print(type(q),type(w),type(e))

#数据字典转换类型

i =10
#转换为浮点型
print(float(i))
u =1.0
#把浮点型转换为int型
print(int(u))
print(complex(u))

r=8 % 3
print(r)


