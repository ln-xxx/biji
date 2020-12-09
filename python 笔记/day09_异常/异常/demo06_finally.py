"""
    捕获异常:
        语法:

        try:
            可能发生异常的代码

        except 异常类型1:
            处理异常

        except 异常类型2:
            处理异常

        except 异常类型3 as e:
            处理异常

        .............

        except:
        或者
        except Exception as e:
            处理异常

        else:
            不发生异常,执行else(可以有,可以没有)

        finally:
            最后执行,无论是否发生异常都会执行...
            不会被break打断.....

"""

# 获取键盘输入一个整数, 让这个整数+10, 然后输出

while True:
    num = input("请输入一个整数")
    try:
        num = int(num)  # -9
        num = num + 9   # 0
        print(num)

    except Exception as e:
        print("Exception的子孙", e, type(e))

    else:
        print("如果没有发生异常, 则执行else....")
        break  # break不会打断finally的执行

    # 无论是否发生异常,都会执行finally
    finally:
        print("finally.......")



