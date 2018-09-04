age = int(input("请输入你家猫的年龄:"))

print("")

if age < 0:
    print("不可能的")
elif age ==1:
    print("他还小:",age)
    people =age+17
    print("人的年龄:",people)
elif age >2:
    print("年龄:",age)
    i=(age-1)*2
    people =24+age*2
    print(i)
    print("人的年龄",people)

# elif age >=3:
#     print("他多大了"+age)
else:
    print("没有出生呢")

input("按回车退出")
