import mysql.connector
import configparser
from model.employee import Employee


class Database(object):  # 数据库操作
    @classmethod  # 该注解表示类的方法，优先加载
    def create_connection(cls):
        config = configparser.ConfigParser()
        config.read('model/config.ini')
        USER = config.get('DB_SECTION', 'user')
        PASSWORD = config.get('DB_SECTION', 'password')
        DATABASE = config.get('DB_SECTION', 'database')
        connection = mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE)
        # connection = mysql.connector.connect(user='root', passwd='xc920722', database='demo')
        return connection

    @classmethod
    def query(cls):
        sql = 'select * from employee'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        cursor.close()
        conn.close
        return result_set

    @classmethod
    def query_by_id(cls, id):
        sql = 'select * from employee where id = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [id])
        result_set = cursor.fetchall()
        cursor.close()
        conn.close
        if len(result_set) == 0:
            return None
        else:
            return result_set[0]

    @classmethod
    def query_by_args(cls, code, name):
        sql = 'select * from employee where code = %s and name = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (code, name))
        result_set = cursor.fetchall()
        cursor.close()
        conn.close
        return result_set

    @classmethod
    def save(cls, emp):
        sql = 'insert into employee (code, name) values (%s, %s)'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (emp.code, emp.name))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def update(cls, emp):
        sql = 'update employee set code = %s, name = %s where id = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (emp.code, emp.name, emp.id))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def delete(cls, id):
        sql = 'delete from employee where id = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [id])
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__man__':
    # db = Database()
    # db.create_connection()

    # Database.create_connection()

    # Query
    print(Database.create_connection())
    # print(Database.query())

    # Save
    # employee = Employee('E01', 'Sean')
    # Database.save(employee)

    # Update
    # employee = Employee('E01-updated', 'Sean-updated')
    # employee.id = 1
    # Database.update(employee)

    # Delete
    # Database.delete(1)
