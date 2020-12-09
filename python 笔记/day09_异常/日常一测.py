"""
有三种动物animal：狗dog、猫cat、猪pig，
    父类：动物、
    子类：狗、猫、猪

    动物的属性：动物的名字
    动物的方法是eat（就是打印自己的名字）

有一个饲养员：饲养员feeder

    饲养员的方法：feed_animal(需要饲养的动物)
    函数的实现是（其实就是调用动物的eat方法）

创建对象-->调用方法:
饲养员韩哲喂一下猪	写一下执行结果
韩哲喂一下狗	写一下执行结果
韩哲喂一下猫	写一下执行结果
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃")


class Dog(Animal):
    def eat(self):
        print("我是狗,我叫%s,我吃骨头,偶尔多管闲事吃个耗子" % self.name)


class Cat(Animal):
    def eat(self):
        print("我是猫,我叫%s,我爱吃小鱼儿,偶尔跟狗打架抢耗子" % self.name)


class Pig(Animal):
    def eat(self):
        print("我是猪, 我叫%s,我爱吃西瓜,偶尔在取经的路上看猫狗打架抢耗子" % self.name)


class Feeder:
    def __init__(self, name):
        self.name = name

    def feeder_animal(self, obj):  # obj喂养的动物
        print(self.name+"喂的:")
        obj.eat()


dog = Dog("旺财")
cat = Cat("加菲猫")
pig = Pig("八戒")

f = Feeder("韩哲")
f.feeder_animal(pig)  # 我是猪....
f.feeder_animal(dog)  # 我是狗....
f.feeder_animal(cat)  # 我是猫....







