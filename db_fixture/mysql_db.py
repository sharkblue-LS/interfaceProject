import os
import configparser as cparser
from pymysql import connect,cursors
from pymysql.err import OperationalError
import time

# ======== 读取db_config.ini文件设置 ========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + '/db_config.ini'

cf = cparser.ConfigParser()
cf.read(file_path)


host = cf.get('mysqlconf','host')
port = cf.get('mysqlconf','port')
db = cf.get('mysqlconf','db_name')
user = cf.get('mysqlconf','user')
password = cf.get('mysqlconf','password')

# ======== 封装MySQL基本操作 ========
class DB:
	def __init__(self):
		try:
			#连接数据库
			self.conn = connect(host=host,
			                    user=user,
			                    password=password,
			                    db=db,
			                    charset='utf8',
			                    cursorclass=cursors.DictCursor)
		except OperationalError as e:
			print('Mysql Error %d: %s'%(e.args[0],e.args[1]))
			
	#清除表数据
	def clear(self,table_name):
		real_sql = 'delete from '+table_name + ';'
		with self.conn.cursor() as cursor:
			cursor.execute('set FOREIGN_KEY_CHECKS=0;')
			self.conn.commit()
			cursor.execute(real_sql)
		self.conn.commit()
		
	#插入表数据
	def insert(self,table_name,table_data):
		for key in table_data:
			table_data[key] = "'"+str(table_data[key])+"'"
		key = ','.join(table_data.keys())
		value = ','.join(table_data.values())
		real_sql = "INSERT INTO "+table_name+"("+key+") VALUES("+value+");"
		
		with self.conn.cursor() as cursor:
			cursor.execute(real_sql)
		
		self.conn.commit()
		
	#关闭数据库连接
	def close(self):
		self.conn.close()
		
if __name__ == '__main__':
	create_time = time.strftime('%Y-%m-%d %H:%M:%S')
	print(create_time)
	db = DB()
	table_name = 'sign_event'
	data = {'id':12,'name':'小米mix4发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2021-08-16 18:00:00','create_time':create_time}
	db.clear(table_name)
	db.insert(table_name,data)
	db.close()
		