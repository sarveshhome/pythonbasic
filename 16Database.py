
import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=127.0.0.1,1433;"
    "DATABASE=AuthSystemDb;"
    "UID=sa;"
    "PWD=Strong.Pwd-123;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Connection Timeout=30;"
)

try:
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION, DB_NAME()")

        row = cursor.fetchone()

        print("Connected to SQL Server successfully!")
        print("Database:", row[1])
        print("SQL Server version:", row[0])

except pyodbc.Error as error:
    print("Database connection failed:")
    print(error)
