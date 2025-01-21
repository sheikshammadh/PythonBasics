import mysql.connector
dbcon=None
cursor =None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='jandb')
    cursor=dbcon.cursor()
    sql_st=''' 
                    insert into employee values(1,'shyam',23743.23);      
            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print('Table Created Successfully')
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()