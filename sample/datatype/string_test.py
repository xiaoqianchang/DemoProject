#!/usr/bin/python3
import sys

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

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

