import pymysql

mysql_config = {
    'host': 'your service host',
    'user': 'your username',
    'password': 'your password',
    'database': 'your database',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}


class Mysql:
    # 构造函数
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(**mysql_config)

        # 创建游标对象
        self.cursor = self.conn.cursor()

    def query(self, sql):
        return self.cursor.execute(sql)

    def __del__(self):
        # 释放游标对象
        self.cursor.close()
        # 关闭 mysql 的连接
        self.conn.close()

