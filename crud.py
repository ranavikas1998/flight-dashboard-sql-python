import pyodbc

# Connection setup
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-A4VIG2K\\SQLEXPRESS;'
        'DATABASE=indigo;'
        'Trusted_Connection=yes;' ,  # if using Windows Authentication
        autocommit=True  # with out autocommit it can not create
    )
    cursor = conn.cursor()
    print("✅ Connection established successfully!")

except Exception as e:
    print(" Connection error:", e)

# create  a database  on the db server
#cursor.execute("CREATE DATABASE indigo;")
#conn.commit()

# create a  table
#airport -> airport_id |code | name
#cursor.execute("""
#CREATE TABLE airport(
#    airport_id INTEGER PRIMARY KEY,
#    code       VARCHAR(10) NOT NULL,
#    city       VARCHAR(50)  NOT NULL,
#   name VARCHAR(255) NOT NULL
#)
#""")
#conn.commit() # means  permanently saved

# Insert data to the  table
#cursor.execute("""
#    INSERT INTO airport VALUES
#    (1,'DEL','New Delhi','IGIA'),
#    (2,'CCU','Kolkata','NSCA'),
#    (3,'BOM','Mumbai','CSMA')
#""")
#conn.commit()

# search/Retrieve data
#cursor.execute("SELECT * FROM airport WHERE airport_id>1")
#data=cursor.fetchall()  # means multiple rows
#print(data)

#for i in data: # for  picking the specifie value
#    print(i[3])  # i want to  pick  name inside to the tuple

# Update
#cursor.execute("""
#UPDATE airport SET city='Bombay' WHERE airport_id=3
#""")
#conn.commit()

# again fetch data
#cursor.execute("SELECT * FROM airport")
#data =cursor.fetchall()
#print(data)

# delete
#cursor.execute("DELETE FROM airport WHERE airport_id=3")
#conn.commit()

#cursor.execute("SELECT * FROM airport")
#data=cursor.fetchall()
#print(data)

