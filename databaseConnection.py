import psycopg2 as database
import sys 

#Function to connect the app to the database, the data base is in postgresql.
#Info:
#Database = danielcompany
#user     = localhost
#Password = ' ', this is because the database does not have a password, this is a lack of security
#Host     = localhost or 127.0.0.1
#If the connection fail, the code prevent this connection with a exception.
def connectionToDatabase():
    try:
        conn = database.connect(database="danielcompany", user="danielflores", password="pruebatecnica", host="localhost", port = "5433")
        cursor = conn.cursor()
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("Conexion bien", file = sys.stderr)
        return conn
    except (Exception, database.DatabaseError) as error:
        rint(error)
