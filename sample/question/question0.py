# 测试文档格式及输出
def a():
    """这是文档"""
    pass


print(a.__doc__)

# 二进制、八进制、十六进制转换
b = 0b00111100
print(b)
c = 60
print(bin(c))  # bin返回一个整数的二进制字符串，以0b开头
print(oct(c))  # 输出八进制
print(hex(c))  # 输出十六进制

d = 1000
e = 1000
print(id(d))
print(id(e))
