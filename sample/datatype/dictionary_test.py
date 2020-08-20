#!/usr/bin/python3
# Dictionary（字典）

dict_test = {}  # 创建空字典
dict_test['one'] = "1 - 菜鸟教程"
dict_test[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict_test['one'])  # 输出键为 'one' 的值
print(dict_test[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


# 构造函数 dict() 创建一个字典
# 构造函数 dict() 可以直接从键值对序列中构建字典
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))  # 元素为元组的列表
print(dict({('Runoob', 1), ('Google', 2), ('Taobao', 3)}))  # 元素为元组的集合
print(dict([['Runoob', 1], ['Google', 2], ['Taobao', 3]]))  # 元素为列表的列表
print(dict((('Runoob', 1), ('Google', 2), ('Taobao', 3))))  # 元素为元组的元组
print({x: x**2 for x in (2, 4, 6)})
print(dict(Runoob=1, Google=2, Taobao=3))


def example(a, b):  # 函数返回多个值的时候，不一定是以元组的方式返回的，还要看自己定义的返回形式是什么。
    return a, b


def example2(a, b):
    return [a, b]


print(type(example(3, 4)))
print(type(example2(3, 4)))


def test(*args):  # 函数还可以接收可变长参数，比如以 "*" 开头的的参数名，会将所有的参数收集到一个元组上。
    return args


print(test(1, 2, 3, 4))
print(type(test(1, 2, 3, 4)))


def sample(d):  # 对字典进行for遍历，遍历的是字典的键，而不是值。
    for c in d:
        print(c)


print(sample(dict(Runoob=1, Google=2, Taobao=3)))


def sample2(d):  # 对字典进行for遍历，遍历的是字典的键，而不是值。
    for c in d:
        # print(c, ':', dict[c])
        print(c, end=':')
        # print(dict.keys())
        print()


sample2(dict(Runoob=1, Google=2, Taobao=3))


dict1 = {'abs': 1, 'cde': 2, 'd': 4, 'c': 567, 'd': 'key1'}
print(dict1.items())  # 对于重复的键，后面的value会覆盖前面的value
print(dict1.keys())
print(dict1.values())
for k, v in dict1.items():
    print(k, ':', v)


"""
字典推导式
"""
p = {i: str(i) for i in range(1, 5)}
print('p:', p)

x = ['A', 'B', 'C', 'D']
y = ['a', 'b', 'c', 'd']
n = {i: j for i, j in zip(x, y)}
print('n:', n)

s = {x: x.strip() for x in ('he', 'she', 'I')}
print('s:', s)

