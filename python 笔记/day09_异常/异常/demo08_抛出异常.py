"""
    抛出异常:
        创建异常对象,并由程序员手动抛出
        关键字 raise
        Exception类的对象
"""


# 让用户输入密码,如果密码长度小于8,抛出异常打断程序的执行

password = input("请输入长度至少为8的密码:")

try:
    if len(password) < 8:
        # 创建异常对象
        e = Exception("长度忒短了, 容易被盗")
        # 并抛出
        raise e
    #raise TypeError('xxxxxxxx') #

except Exception as e:
    print(type(e), ":", e)
else:
    # 如果没有发生异常,则执行else
    print("您的密码设置成功!")










