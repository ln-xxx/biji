"""
    多态: 多种形态

    issubclass(参数1, 参数2)  参数1是否是参数2的子类

数值类型: 整数int 浮点数float 复数complex 布尔类型bool True/False
"""

s = "abc"
print(type(s))   # <class 'str'>
print(isinstance(s, str))  # True


class A:
    pass


class B(A):
    pass


a = A()
print(isinstance(a, A))  # True

b = B()   # B类的对象
print(type(b))  # <class '__main__.B'>
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True

# 两个参数必须都是类, 判断参数1类是否是参数2类的子类
print(issubclass(B, A))  # True




