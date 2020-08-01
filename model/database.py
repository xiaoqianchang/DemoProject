import mysql.connector


class Database(object):  # 数据库操作
    def create_connection(self):
        connection = mysql.connector.connect(user='root', password='', database='demo')
        return connection


if __name__ == '__man__':
    db = Database()
    db.create_connection()