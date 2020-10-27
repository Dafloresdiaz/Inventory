import psycopg2 as database
from flask import Flask, render_template, request
import sys

app = Flask(__name__)
app.debug = True

#The methods in a list to not repeat the same code.
allmethods = ['GET', 'POST']
getMethod = ['GET']

#All the views for each page in the app, the pages are in templates for any future modification.
@app.route("/", methods=getMethod)
def homePageView():
    return render_template("index.html")

@app.route("/createNewStore", methods=allmethods)
def createNewStoreView():
    return render_template("addStore.html")

@app.route("/createNewInventory", methods=allmethods)
def createNewInventoryView():
    return render_template("addInventory.html")

@app.route("/addNewProductToAInventory", methods=allmethods)
def createNewProductView():
    return render_template("addProduct.html")

@app.route("/deleteProduct", methods=allmethods)
def deleteAProduct():
    return render_template("deleteProduct.html")

@app.route("/stockForAProduct",methods=getMethod)
def stockProducts():
    return render_template("stockProducts.html")

#Function to connect the app to the database, the data base is in postgresql.
#Info:
#Database = danielcompany
#user     = localhost
#Password = ' ', this is because the database does not have a password, this is a lack of security
#Host     = localhost or 127.0.0.1
#If the connection fail, the code prevent this connection with a exception.
def connectionToDatabase():
    try:
        conn = database.connect(database="danielcompany", user="localhost", password=' ', host="localhost")
        cursor = conn.cursor()
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("Conexion bien", file = sys.stderr)
        conn.close()
    except (Exception, database.DatabaseError) as error:
        print(error)

connectionToDatabase()

