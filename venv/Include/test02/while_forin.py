#100的和
num =100
count =1
sum = 0

# while count<=num:
#     sum+=count
#     count=count+1
#
# print(sum)

# while count<=num:
#     if count%2!=0:
#         print(count)
#
#     count=count+1

# while count<=5:
#     print(count)
#     count+=1
# for x in range(1,10):
#     for i in range(1,10-x):
#         print(" ",end="")
#     for c in range(1,x+1):
#         print("* ", end="")
#
#     print()
#for in 循环中可以遍历列表
list =[1,2,3,4]
for i in list:
    print(i)

#for in 循环遍历字典 dictionary
dic ={"name":"小明","age":12}
for x in dic.items():
    print(x)

#for in 遍历元祖
tup =(1,2,'aaa','bbbb')
for q in tup:
     print(q)

#break 与 continue 的区别
#break：break是跳出循环
#continue:continue是跳出本次循环，继续循环

#break实例
for e in range(5):
    if e == 4:
        break
    print(e)

print('------------')
#continue实例
for t in tup:
    if t =='aaa':
        continue
    print(t)

for r in range(1,20,4):
    print(r)





