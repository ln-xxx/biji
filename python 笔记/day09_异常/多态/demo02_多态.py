"""
    多态:
        以继承和重写为前提, 创建不同的对象, 执行不同的方法

python弱类型的语言:
    声明一个对象时,不需要标注这个对象的类型,
    在给这个对象赋值时, python解释器会自动的根据所赋值的类型,定义变量的类型
    这个对象的类型可以根据赋值不同而发生改变

    a = "abc"  # str
    a = A()  # A

强类型语言:
    int a
    a = 100

    Person --> Student

    Person p = Person()
    Person s = Student()

"""


class Father:
    def say(self):
        print("儿子, 快点回来吃饭....")


class Son(Father):
    def say(self):
        print("我要和小花玩, 你们先吃吧")


f = Father()
f.say()

s = Son()
s.say()


def talk(obj):  # obj 参数
    if isinstance(obj, Father):  # 儿子类对象 父亲类的对象
        obj.say()  # 不同的say方法
    else:
        print("不是爹和儿子, 闭嘴...")


print("---------------")
talk(123)
talk(f)
talk(s)

