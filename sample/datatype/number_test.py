"""
Number 中包含 int float bool complex
"""

# True 被当作 1，False 被当作 0
print(True + 2)
print(False + 2)

# 其他类型值转换 bool 值时除了 ''、""、''''''、""""""、0、()、[]、{}、None、0.0、0L、0.0+0.0j、False 为 False 外，其他都为 True
print(bool(-2))
print(bool(''))
