#六个数据类型之---Set（集合）
#集合（set）是一个无序不重复元素的序列,案例

#创建一个set
student = {'小明','小红','小花','小明','aa','小丽'}
#输出会输出不重复无序的结果
print(student)



a =set('aaddcc')

b =set('ddeeffgg')
print(a,end="")
print(b)

#取ab的差集
print(b-a)
#a与b不存在的元素
print(b^a)
#a与d的交集
print(a&b)

