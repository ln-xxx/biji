"""
  用户输入整数, 让整数+10, 再输出
  如果用户输入的是整数或可以看做整数, 直接+10再输出
  如果用户输入的是其他的,&*#%@%....,重新输入,直到输入正确为止


  语法:
        try:
            可能发生异常的代码
        except 异常的类型1:
            处理异常
        except 异常的类型2:
            处理异常
        .......
        else:
            如果没有发生异常,则执行else.....
"""
while True:
    a = input("请输入一个整数:")  # a --> str  int("110") --> 110
    try:
        a = int(a)
        res = a + 10
        print(res)   # 100
    except ValueError:
        print("您输入有误, 请重新输入")
        # 重新输入
    else:
        print("没有发生异常.......")  # 执行
        break






