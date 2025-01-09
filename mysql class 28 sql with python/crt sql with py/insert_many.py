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
    sql_st = '''INSERT INTO employee(eid,name,esal) values(%s,%s,%s)'''
    users=[(103,'priya',75000.70),(104,'sushma',87252.25),(105,'nandu',2352.54)]
    cursor.execute(sql_st,users)
    dbcon.commit()
    print("Data inserted successfully")
except mysql.err:
    print(f"Unable to insert: {err}")
finally:
    if cursor is not None:
        cursor.close()
    if dbcon is not None:
        dbcon.close()

