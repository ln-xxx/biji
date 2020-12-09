"""
    自定义异常

    自己定义一个异常类，继承Exception类, 捕获下面的过程：
    判断input()输入的字符串长度是否小于8， 如果小于8，
    比如输入长度为3则输出:" The input is of length 3,
    expecting at least 8’，大于8输出"print success' 

    1. 给出产生异常的条件
    2. 创建异常对象
    3. raise 抛出异常对象

"""


class MyException(Exception):
    def __init__(self, input_len, at_least):
        # 用户输入的长度
        self.input_len = input_len
        # 程序规定的最小长度
        self.at_least = at_least
count = 0        
while count < 3:        


    password = input("请你输入一个长度至少为8的密码")


    try:
        input_len = len(password)
        if input_len < 8:
            # 创建异常对象 并抛出
            e = MyException(input_len, 8)
            raise e

    except MyException as e:
        print("The input is of length %d,"
              "expecting at least %d" % (e.input_len, e.at_least))
        count += 1
        if count == 3:
            choice = input('是否继续 ,y/n')
            if choice == 'y':
                count = 0
            else:
                print('忘记密码')
            

    else:
        print("您密码设置成功")
        break
    
    finally:
        print('ok')





