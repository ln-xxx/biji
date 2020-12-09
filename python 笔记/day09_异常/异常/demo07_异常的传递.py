"""
    异常的传递:
        如果函数中产生了异常,函数中没有处理,会将异常传递给调用处
        如果调用处也没有处理,则会抛出异常对象吗,打断程序的执行

"""


def get_input():
    num = input("请输入一个整数:")
    num = int(num)
    print(num)


def get_input_two():
    get_input()


try:
    get_input_two()
except ValueError as e:
    print(e)





