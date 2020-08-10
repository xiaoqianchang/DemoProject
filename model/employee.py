# 对象
class Employee(object):  # pass 类似于todo
    def __init__(self, code, name):
        # 1. positional arguments
        # 2. *args Non-keyword arguments　　　---　　　tuple(x,x,x)　　　（可变参数，类似java的可变参数，可以０到ｎ个）
        # 3. **kwargs keyword arguments   ---   dict{key.value}
        # 4. ＊, keyword only arguments
        self.code = code
        self.name = name
    # def __init__(self, code, name, salary, **args):
    #     # 1. positional arguments
    #     # 2. *args Non-keyword arguments　　　---　　　tuple(x,x,x)　　　（可变参数，类似java的可变参数，可以０到ｎ个）
    #     # 3. **kwargs keyword arguments   ---   dict{key.value}
    #     # 4. ＊, keyword only arguments
    #     self.code = code
    #     self.name = name
    #     self.details = args
    #     self.salary = salary
    #     print(args)


# if __name__ == '__main__':  # class 方法定义 后面空两行
#     # employee = Employee('E01', 'Sean Xiao')
#     # employee = Employee(code='E01', name='Sean Xiao', email='123@gmail.com')
#     data = {'email': '123@gmail.com', 'phone': 12345}
#     # employee = Employee('E01', 'Sean Xiao', salary=0.0, **data)
#     employee = Employee('E01', 'Sean Xiao', salary=0.1, **data)
#     print(employee)
#     print(employee.code)
#     print(employee.name)
#     print(employee.details.get('email'))
#     print(employee.details.get('phone'))
#     print(employee.salary)


# employee = Employee()
# employee.age = 18
# employee.sex = '男'
# employee.code = 'E01'
# employee.name = 'Sean Xiao'
# print(employee)
# print(employee.code)
# print(employee.name)