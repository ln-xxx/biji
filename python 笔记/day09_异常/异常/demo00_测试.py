"""
(<class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
(<class 'NameError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
(<class 'IndexError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
(<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

"""

print(ValueError.__mro__)
print(NameError.__mro__)
print(IndexError.__mro__)
print(ZeroDivisionError.__mro__)
