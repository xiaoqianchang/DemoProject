#!/usr/bin/python3

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组


tup = (1, 2, 3, 4, 5, 6)
print(tup[0])  # 输出元组的第一个元素 ==1
print(tup[1:5])  # 输出从第二个元素开始到第五个元素 ==(2, 3, 4, 5)
print(tup[1:])  # 输出从第二个元素开始到最后一个 ==(2, 3, 4, 5, 6)
print(tup[1:-1])  # 与 tup[1:5] 一样 ==(2, 3, 4, 5)
print(tup[-3:-2])  # 输出 ==(4,)
# tup[0] = 11  # 修改元组元素的操作是非法的
print(tup[1::2])  # 从索引为 1 的元素开始 每隔2个元素取一次元素 ==(2, 4, 6)
print(tup[1::-1])  # 从索引为 1 的元素开始到列表尾倒序 ==(2, 1)
print(tup[-1::-1])  # 从列表尾开始到列表头倒序 ==(6, 5, 4, 3, 2, 1)


tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup)
print(tup1)
print(tup2)
