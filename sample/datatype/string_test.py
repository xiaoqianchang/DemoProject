#!/usr/bin/python3
import sys
from collections import Counter  # 以字典的形式，输出每个字符串中出现的字符及其数量

'''
字符串截取
'''
str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

# 0、a,b为参数。从字符串指针为a的地方开始截取字符，到b的前一个位置（因为不包含b）
var1 = "hello world"

# 1、如果a,b均不填写，默认取全部字符。即，下面这两个打印结果是一样的
print(var1[:])  # hello world
print(var1)     # hello world

# 2、如果a填写，b不填写（或填写的值大于指针下标），默认从a开始截取，至字符串最后一个位置
print(var1[3:])  # lo world

# 3、如果a不填写， b填写，默认从0位置开始截取，至b的前一个位置
print(var1[:8])  # hello wo

# 4、如果a为负数，默认从尾部某一位置，开始向后截取
print(var1[-2:])  # ld

# 5、如果a>=b, 默认输出为空。
print(var1[3:3])
print(var1[3:2])

# 6、步长
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L[::2])

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input("\n\n按下 enter 键后退出。")

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# !/usr/bin/python3

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:  # sys.argv 是命令行参数列表。
    print(i)  # 输出当前文件的绝对路径
print('\n python 路径为', sys.path)

print("hello ' world!")

a = '2.1'
print(int(float(a)))

'''
字符串格式化
'''
name = '小明'
address = '上海'
result1 = 'Hello %s，welcome to %s' % (name, address)
result2 = 'Hello {}，welcome to {}'.format(name, address)
result3 = 'Hello {0}，welcome to {1}'.format(name, address)
result4 = 'Hello {name}，welcome to {address}'.format(name=name, address=address)
result5 = f'Hello {name}，welcome to {address}'
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

num = 56
print('二进制：', bin(num))
print('八进制：%o' % num)
# print('十进制：%o' % num)
print('十六进制：%x' % num)

x = 1
print(f'{x + 1 = }')

'''
Counter 使用
'''
# 定义两个字符串变量
Var1 = "1116122137143151617181920849510"
Var2 = "1987262819009787718192084951"

# 以字典的形式，输出每个字符串中出现的字符及其数量
print(Counter(Var1))
print(Counter(Var2))
