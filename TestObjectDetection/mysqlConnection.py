from datetime import datetime

import mysql.connector
mydb = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password = 'root',
    port = '3306',
    database = 'object_detection'

)
mycursor = mydb.cursor()
query = f"INSERT INTO `object_detection`.`object_detected` (`object_name`, `time`) VALUES ( 'toffee', '{datetime.now()}');"

print(query)
mycursor.execute(query)

mycursor.execute('select * from object_detected')
dataFeteched = mycursor.fetchall()

for data in dataFeteched:
    print(data)
