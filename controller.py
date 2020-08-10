from webhandler import get, post
from model.database import Database
from model.employee import Employee


@get('/')
def index():
    return {
        '__template__': 'employee_list.html'
    }


# 查询所有数据
@get('/services/employees')
def get_employees():
    emps = Database.query()
    return dict(employees=emps)


# ADD按钮点击后的页面
@get('/ui/employees/add')
def ui_add_employee():
    return {
        '__template__': 'add_edit_employee.html',
        'id': '',
        'action': '/services/employees'
    }


# SAVE按钮点击后的Action
@post('/services/employees')
def add_employee(*, code, name):
    employee = Employee(code, name)
    Database.save(employee)


# 编辑按钮点击后的页面（如果注释掉会报 404: Not Found）
@get('/ui/employees/edit')
def ui_edit_employee(*, id):
    return {
        '__template__': 'add_edit_employee.html',
        'id': id,
        'action': '/services/employees'
    }


# 编辑时带回数据并显示在输入框里
@get('/services/employees/{id}')
def get_employee(*, id):
    employee = Database.query_by_id(id)
    print(employee)
    return dict(id=employee[0], code=employee[1], name=employee[2])


# 编辑点击后点击SAVE后的Action
@post('/services/employees/{id}')
def update_employee(*, id, code, name):
    employee = Employee(code, name)
    employee.id = id
    Database.update(id)


# delete按钮点击后的Action
@post('/services/employees/{id}/delete')
def delete_employee(*, id):
    Database.delete(id)