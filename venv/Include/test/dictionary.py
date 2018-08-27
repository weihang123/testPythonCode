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
#输出所有values
print(dic.values())

a=dict([('name','小明')])
print(a)
dict_a={'Runoob':1, 'aaa':2, 'dddd':3}
e=dict_a['aaa']

