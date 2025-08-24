from sqlalchemy import create_engine
import pandas as pd
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

#create  a database  on the db server
cursor.execute("CREATE DATABASE flights;")
conn.commit()

# Load Excel data
df = pd.read_excel("flights_cleaned.xlsx")

# Create SQLAlchemy engine (pointing to flights DB)
engine = create_engine(
    "mssql+pyodbc://DESKTOP-A4VIG2K\\SQLEXPRESS/flights?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# Push dataframe to SQL Server
df.to_sql("flights", engine, if_exists="replace", index=False)
print("✅ Data inserted into 'flights' database, table 'flights_table'")