#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了

# num =0
# def test():
#     global num
#     print(num)
#     num=123
#     print(num)
# test()

#不用nonlacal输出结果是：100,10

# def outer():
#     num =10
#     def inner():
#         num =100
#         print(num)
#     inner()
#     print(num)
# outer()

#使用nonlacal来进行修改外层非全局变量
def outer():
    num =5
    print(id(num))
    def inner():
        nonlocal num
        num =8
        print(id(num))
        print(num)
    inner()
    print(num)
outer()
