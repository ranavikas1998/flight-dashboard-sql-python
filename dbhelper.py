import pandas as pd
import pyodbc

class DB:
    def __init__(self):
        # connect to the database
        # Connection setup
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=DESKTOP-A4VIG2K\\SQLEXPRESS;'
                'DATABASE=flights;'
                'Trusted_Connection=yes;',  # if using Windows Authentication
                autocommit=True  # with out autocommit it can not create
            )
            self.cursor = self.conn.cursor()
            print("✅ Connection established successfully!")

        except Exception as e:
            print(" Connection error:", e)


    def  fetch_city_names(self):
        city=[]
        self.cursor.execute("""
        select  distinct(Destination)  from  flights
        union
        select  distinct(source)  from  flights
        """)


        data=self.cursor.fetchall()

        for item  in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self,source,destination):
        self.cursor.execute("""
        SELECT  Airline,Route,Dep_Time,Duration FROM  flights WHERE  source ='{}' AND  destination='{}'
        """.format(source,destination))  #  passing the string  value through  the  format function

        data=self.cursor.fetchall()

        return data

    def fetch_airlines_frequency(self):
        airline=[]
        frequency=[]
        self.cursor.execute("""
        SELECT  airline ,count(*)  FROM flights GROUP BY airline
        """)

        data=self.cursor.fetchall()

        for item in  data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency   #  frequency means count values in  my database

    def  busy_airport(self):
        city=[]
        frequency=[]
        self.cursor.execute("""
        SELECT Source,COUNT(*)  FROM (SELECT Source FROM flights
                               UNION ALL
							   select Destination FROM flights) t
        GROUP BY T.Source
        ORDER BY  COUNT(*) DESC
        """)

        data=self.cursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency