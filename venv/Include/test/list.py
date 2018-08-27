#六个数据类型之---List(列表)
#列表是写在[]里面的，如 变量名 = [数据]
#list截取字符串与String一致，[]数据类型可以不相同

#创建一个列表
list = [123,'This is List',12.98,223232]

#输出这个list
print(list)
#输出第一个元素
print(list[0])
#从第二个开始到第三
print(list[1:3])
#从第二个开始一直到结束
print(list[2:])
#从第3个元素开始输入2次列表
print(list[3:] * 2)



#list与String不一样的是list可以改变而String不能更改值 案例如下：

updata = [1,2,3,8,6,4,5,'qwer']
#更改第最后一个元素的值
updata[-1] ='zxcv'
#更改第2个元素到第五个元素
updata[2:5] = [0,'d',67.03]
#打印更改的结果
print(updata)

#list之间的拼加用“+”

add =list+updata
#打印拼加的list
print(add)

lit =[]
print(lit)

