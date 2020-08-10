import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="xc920722",   # 数据库密码
  database="demo"
)

# 测试数据库连通性
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select * from employee")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
  print(x)