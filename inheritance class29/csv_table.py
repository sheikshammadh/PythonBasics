import mysql.connector

dbcon = None
try:
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='6pm'
    )
    cursor = dbcon.cursor()
    sql_st = '''INSERT INTO products VALUES (product id,product name,price,category);'''
    cursor.execute(sql_st)
    dbcon.commit()
    
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(f"Unable to insert: {err}")
