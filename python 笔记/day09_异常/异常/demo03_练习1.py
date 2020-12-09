"""
1. 预处理的操作

2. 程序员处理不了的问题

"""


try:
    a = "a"
    print(b)
except NameError:
    print("没有这个变量")


print("-----------------------------")


s = "今天下午表彰大会:心态决定命运,自信走向成功"

try:
    index = 0
    while index < len(s):
        print(s[index])
        index += 1
except IndexError:
    print("索引越界")


print("-----over-----")




