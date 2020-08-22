"""
Number 中包含 int float bool complex
"""
import random  # 随机数
import operator  # cmp 函数替代者
from fractions import Fraction  # fractions 模块提供分数类型的支持
import decimal  # decimal 模块提供了一个 Decimal 数据类型用于浮点数计算

# True 被当作 1，False 被当作 0
print(True + 2)
print(False + 2)

# 其他类型值转换 bool 值时除了 ''、""、''''''、""""""、0、()、[]、{}、None、0.0、0L、0.0+0.0j、False 为 False 外，其他都为 True
print(bool(-2))
print(bool(''))

print(round(10.5))
print(round(11.5))

print(random.choice(range(10)))  # 从0到9中随机挑选一个整数
print(random.randint(1000, 9999))
print(random.random())

list = random.sample('abcd1234', 4)  # temp 为 list
print(''.join(list))

print(round(10.44))  # 10
print(round(10.50))  # 10
print(round(10.64))  # 11
print()
print(round(11.44))  # 11
print(round(11.50))  # 12
print(round(11.64))  # 12

print(round(1.45, 1))
print(round(1.55, 1))
print(round(1.15, 1))
print(round(1.50, 0))
print(round(2.50, 0))

'''
复数
字符串拼接
'''
a = 4.1 + 0.3j
print(a)
s1 = '实数：{}, 虚数：{}'.format(a.real, a.imag)  # {}做占位符
s2 = '实数：{0}, 虚数：{1}'.format(a.real, a.imag)  # 对号入座-序列号
s3 = '实数：{real}, 虚数：{imag}'.format(real=a.real, imag=a.imag)  # 对号入座-key-value
print(s1)
print(s2)
print(s3)

'''
cmp(x, y) 函数替代者
'''
operator.gt(1, 2)      # 意思是greater than（大于）
operator.ge(1, 2)      # 意思是greater and equal（大于等于）
operator.eq(1, 2)      # 意思是equal（等于）
operator.le(1, 2)      # 意思是less and equal（小于等于）
operator.lt(1, 2)      # 意思是less than（小于）

'''
分数
'''
x = Fraction(1, 3)
y = Fraction(4, 6)
print(x + y)
print(Fraction(1, 1))
print(Fraction('0.25'))  # 等同于 Fraction(1, 4)

# 浮点数与分数的转换：
f = 2.5
print(Fraction(*f.as_integer_ratio()))

'''
decimal 模块
提供了一个 Decimal 数据类型用于浮点数计算
'''
decimal.getcontext().prec = 4  # 指定精度（4位小数）
decimal_num1 = decimal.Decimal(1) / decimal.Decimal(7)
print(decimal_num1)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    decimal_num2 = decimal.Decimal('1.00') / decimal.Decimal('3.00')
    print(decimal_num2)

print(decimal.Decimal.from_float(1.05))

'''
数字与字符，列表之间的转换
'''
var = '1234'
print(int(var))  # 字符转为数字
num_list = list(var)  # 字符转为列表
print(num_list)
print([int(i) for i in num_list])
