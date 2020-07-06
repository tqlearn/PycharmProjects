#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接

def opendb(sql):
    try:
        db = pymysql.connect("192.168.10.6", "zhebo.lin", "Zhebo@lin3", "zentao", charset='utf8' )

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句

        cursor.execute(sql)
        #col = cursor.description
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchall()
        return data
    except Exception as e:
        raise
    finally:
        db.close()
def opendbs(sql):
    try:
        db = pymysql.connect("47.94.241.60", "ceshi_read", "ceshi@123", "zentao", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句

        cursor.execute(sql)
        # col = cursor.description
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchall()
        return data
    except Exception as e:
        raise
    finally:
        db.close()
def inssql(sql):
    try:
        db = pymysql.connect("172.16.11.105", "root", "123456", "Zento", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        raise
    finally:
        db.close()

if __name__ == '__main__':
    sql = "SELECT count(id) from zt_bug where resolution = 'fixed' and resolvedDate <= '2020-04-21 16:07:32' and status = 'resolved' and openedBy ='dekai.dang' and deleted = 0  order by resolvedDate desc"
    print(opendb(sql))
    #print(inssql(sql))
