# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
#
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
#
# 键(key)必须使用不可变类型。
#
# 在同一个字典中，键(key)必须是唯一的。

#创建一个dictionary
dic ={'name':'小明','age':12,'height':176.5}

print(dic['name'])
#输出所有key
print(dic.keys())
print(list(dic.keys()))
#输出所有values
print(dic.values())

a=dict([('name','小明')])
print(a)
dict_a={'Runoob':1, 'aaa':2, 'dddd':3}
e=dict_a['aaa']
dic01 =dic.copy()
print("----------")
dic.clear()
print(dic01)

#创建新字典 dict.fromkeys()
tup =("xiaoming","nihao","xuexipython")
i =dict.fromkeys(tup,10)
print(i)
print(str(i))

#获取字段中指定键对应的值，如果没有对应值执行默认值 dict.get("获取字段的key","没有key取默认值")
print(dic01.get("name","没有对应值"))
print("zhi :%s" % dic01.get("name1","没有对应值"))

#查看key是否存在某个key
print("name" in dic01)#True
print("nn" in dic01)#False

print(dic01.items())






