import mysql.connector
import configparser
from model.employee import Employee


class Database(object):  # 数据库操作
    @classmethod  # 该注解表示类的方法，优先加载
    def create_connection(cls):
        config = configparser.ConfigParser()
        config.read('config.ini')
        USER = config.get('DB_SECTION', 'user')
        PASSWORD = config.get('DB_SECTION', 'password')
        DATABASE = config.get('DB_SECTION', 'database')
        connection = mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE)
        return connection

    @classmethod
    def query_employee(cls):
        sql = 'select * from employee'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        cursor.close()
        conn.close
        return result_set

    @classmethod
    def save_employee(cls, emp):
        sql = 'insert into employee (code, name) values (%s, %s)'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (emp.code, emp.name))
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__man__':
    # db = Database()
    # db.create_connection()

    # Database.create_connection()

    # Query
    print(Database.query_employee())

    # Save
    employee = Employee('E01', 'Sean Xiao')
    Database.save_employee(employee)
