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
    sql_st = '''INSERT INTO employee VALUES (102, 'Sonia', 55000.45);'''
    cursor.execute(sql_st)
    dbcon.commit()
    
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(f"Unable to insert: {err}")
finally:
    if cursor is not None:
        cursor.close()
    if dbcon is not None:
        dbcon.close()

