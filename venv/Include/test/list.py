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


list01 =[1,2,3,4,5]
list02 =[6,7,8,9,10]
#查看列表长度
print(len(list01))
#列表拼接
#print(list01+list02)
#list02+=list01
#print(list02)
#打印重复列表
print(list01*2)
#用in查看字符是否在list中存在
print(10 in list01)

#反向列表中的元素 list.reverse()
#list02.reverse()
print(list02)

#移除列表中的某个元素，默认最后一个 list.pop(不填写参数，默认最后一个元素值被删除)
# list02.pop()
# print(list02)

#按照索引位置移除 list.pop(索引位置)
# list02.pop(1)
# print(list02)

#查找10元素在哪个索引位置上list.index(要查询的元素值)
print(list02.index(10))

#在指定位置上插入元素 list.inster(索引位置，插入元素)
list02.insert(2,"我是inster")
print(list02)

# 清空列表 list.clear
# list02.clear()
# print(list02)

#复制列表 list.copy()
list03=list02.copy()
print(list03)

#列表排序 list.sort(按照参数进行排序，比较元素通过该参数进行排序，倒序/正序(默认正序))
list04 =['b','c','a','g','f','e','d']
list04.sort()
print(list04)
#按照降序排序
list04.sort(reverse=True)
print(list04)
#按照正序排序
list04.sort(reverse=False)
print(list04)

#按照指定列表中的元素排序
# def test(elem):
#     return elem[2]
#
# list05 =[(1,4,5),(4,'ni'),(2,1,4),(1,2,3,4)]
#
# list05.sort(key=test)
#
# print(list05)
lis =[1,2,3]
lis01 =[4,5]
lis.extend(lis01)
print(lis)








