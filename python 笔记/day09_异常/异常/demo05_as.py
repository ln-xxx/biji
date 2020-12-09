"""
    as 关键字


"""

# 获取键盘输入一个整数, 让这个整数+10, 然后输出
num = input("请输入一个整数")

try:
    num = int(num)  # -9
    num = num + 9   # 0
    res = 100 / num
    print(res)

# except ValueError as e:
    # print("数据错误, 输入的不是整数.....", e)

# except ZeroDivisionError as e:  # as 对象名(自己取的)
    # print("0不能做除数", e)

# except:  # 捕获所有异常对象
    # print("意想不到的其他错误")

# 捕获所有Exception子孙类的异常对象
except Exception as e:
    print("Exception的子孙", e, type(e))

else:
    print("如果没有发生异常, 则执行else....")







