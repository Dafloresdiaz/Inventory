from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from addStore import addNewStore
from addProduct import addNewProduct
from addProduct import createListStores
import sys

app = Flask(__name__)
app.secret_key = "inventario"
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
    error = None
    if request.method == 'POST':
        if request.form["insertStore"] == "insertStore":
            storeName = request.form["storeName"]
            adress = request.form["Adress"]
            city = request.form["City"]
            phoneNumber = request.form["phoneNumber"]
            if addNewStore(storeName, adress, city, phoneNumber):
                flash("Store correctly inserted", category="info")
                return redirect(url_for('createNewStoreView'))
            else:
                if not storeName:
                    error = "The name of the Store is empty"
                elif not adress:
                    error = "The adress of the store is empty"
                elif not city:
                    error = "The city of the store is empty"
                elif not phoneNumber:
                    error = "The phone of the store is empty"
                else:
                    error = "The Store is already in the database"
                return render_template("addStore.html", error=error)
    else:
        return render_template("addStore.html")

@app.route("/addNewProduct", methods=allmethods)
def createNewProductView():
    listStores = createListStores()
    error = None
    if request.method == 'POST':
        if request.form["insertProduct"] == "insertProduct":
            productName = request.form["productName"]
            typeProduct = request.form["typeProduct"]
            storeSelection = request.form["storeSelection"]
            if addNewProduct(productName, typeProduct, storeSelection):
                flash("Product correctly inserted")
                return redirect(url_for("createNewProductView",storesList = listStores))
            else:
                if not productName:
                    error = "The product name is empty"
                elif not typeProduct:
                    error = "The type of product is empty"
                elif not storeSelection:
                    error = "The selection of the store is empty"
                else:
                    error = "The product is already created and related with a store"
                return render_template("addProduct.html", error=error,storesList = listStores)
    else:
        return render_template("addProduct.html",storesList = listStores)

@app.route("/stockForAProduct",methods=allmethods)
def stockProducts():
    return render_template("stockProducts.html")





