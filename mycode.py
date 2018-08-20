
import pymysql

# Open database connection
connection = pymysql.connect(host = 'localhost',user = 'Soumya',passwd ='password',db ='sampledb')

# prepare a cursor object using cursor() method
cursor = connection.cursor()
# execute SQL query using execute() method.
sql = ("INSERT INTO country(id,state,country,population) VALUES('%d','%s','%s','%d')" % (3,'Alaska','Canada',45678))
cursor.execute(sql)
connection.commit()
# Fetch a single row using fetchone() method.
data = cursor.fetchall()

print(data)
