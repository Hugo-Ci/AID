# import pymysql
#
# db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = '123456',database = 'stu',charset = 'utf8')
# cur = db.cursor()
# sql = 'insert into class values (5,"emma",17,"w",79);'
# cur.execute(sql)
# db.commit()
# cur.close()
# db.close()

# import pymysql
#
# db = pymysql.connect(user = 'root',password = '123456',database = 'stu',charset = 'utf8')
# cur = db.cursor()
# sql = 'select * from interest;'
# cur.execute(sql)
# # for i in cur:
# #     print(i)
#
# # all_row = cur.fetchall()
# # print(all_row)
#
# # many_row = cur.fetchmany(2)
# # print(many_row)
#
# # one_row = cur.fetchone()
# # print(one_row)
#
# cur.close()
# db.close()
#
# import pymysql
#
# db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = '123456',database = 'dict',charset = 'utf8')
# cur = db.cursor()
#
# name = input('name:')
# age = input('age:')
# score = input('score:')
# try:
#     # sql = 'insert into class (name,age,score) values ("%s",%d,%f);'%(name,age,score)
#     sql = 'insert into class (name,age,score) values (%s,%s,%s);'
#     cur.execute(sql,[name,age,score])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
# cur.close()
# db.close()
# import pymysql
#
# db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = '123456',database = 'dict',charset = 'utf8')
# cur = db.cursor()
# f = open('dict.txt')
# sql = 'insert into dict (word,mean) values (%s,%s);'
# for line in f:
#     tmp = line.split(' ',1)
#     word = tmp[0]
#     mean = tmp[1].strip()
#     cur.execute(sql,[word,mean])
# try:
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
# cur.close()
# f.close()
# db.close()

import pymysql

db = pymysql.connect(user = 'root',password = '123456',database = 'stu',charset = 'utf8')
cur = db.cursor()

def zc():
    name = input('请输入用户名：')
    key = input('请设置密码：')
    sql = 'select name from user;'
    cur.execute(sql)
    