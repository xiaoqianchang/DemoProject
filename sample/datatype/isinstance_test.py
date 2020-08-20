# 判断子类对象是否继承于父类
class Father(object):
    pass


class Son:
    pass


if __name__ == '__main__':
    print(type(Son()) == Father)
    print(isinstance(Son(), Father))
    print(type(Son()))
    print(type(Son))
