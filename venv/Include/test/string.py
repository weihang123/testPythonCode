#import sys
#六个数据类型之---String(字符串)
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。
from sys import call_tracing

str ='nihoa'
print(str)
print(str[0:2])
print(* str)
print(str[-5],end="");
print(str[-4],end="")
print(str[-3],end='')
print(str[-2],end='')
print(str[-1])

print('\nnihao')
#不进行转译
print(r'\nsdsd')


# #输出n遍
# a=5
# print('qweasd\n'*a)
#
# print('我要学python')

str ="nihao"+"sdsd\""



if("y" in str):
    print("存在n字母")
else:
    print("不包含字符")
str1="adcdeFASDSDghihj"

#输出字符创中最小的字母
print(min(str1))
#输出字符串中最大的字母
print(max(str1))
#查询字符串的长度
print(len(str1))
#讲字符串中的大写变为小写
print(str1)
print(str1.swapcase())
print(str1.lower())