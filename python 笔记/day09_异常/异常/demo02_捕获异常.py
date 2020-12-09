"""
    捕获异常: 抓 逮
        进行异常的处理, 使程序不被打断能够继续的执行

    语法:
        try:
            有可能发生异常的代码
        except 异常类型:
            处理异常

"""

# 获取键盘输入一个整数, 让这个整数+10, 然后输出
num = input("请输入一个整数")  # 1,str 2,阻塞式

try:
    num = int(num)   # -9
    num = num + 9    # 0
    res = 100 / num  # ZeroDivisionError: division by zero
    print(res)
except ValueError:  # 根据异常的类型 捕获相应类型的异常对象
    # 异常的处理
    print("数据错误, 输入的不是整数.....")
except ZeroDivisionError:
    # 异常的处理
    print("0不能做除数")


print("-----over--------")
