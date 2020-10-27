from flask import Flask, render_template, request, flash, redirect, url_for
from addStore import addNewStore
from addInventory import addNewInventory
from addInventory import createListStores
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
            if addNewStore(storeName):
                flash("Store correctly inserted", category="info")
                return redirect(url_for('createNewStoreView'))
            else:
                if not storeName:
                    error = "The name of the Store is empty"
                else:
                    error = "The Store is already in the database"
                return render_template("addStore.html", error=error)
    else:
        return render_template("addStore.html")

@app.route("/createNewInventory", methods=allmethods)
def createNewInventoryView():
    listStores = createListStores()
    error = None
    if request.method == 'POST':
        if request.form["insertInventory"] == "insertInventory":
            inventoryName = request.form["inventoryName"]
            store = request.form["inventorySelection"]
            if addNewInventory(inventoryName, store):
                flash("Inventory correctly inserted")
                return redirect(url_for("createNewInventoryView",storeList = listStores))
            else:
                if not inventoryName:
                    error = "The name of the inventory is empty"
                elif not store:
                    error = "The selection of the store is empty"
                else:
                    error = "The inventory is already created and related with that store"
                return render_template("addInventory.html",error=error,storeList = listStores)

    else:
        return render_template("addInventory.html", storeList = listStores)

@app.route("/addNewProductToAInventory", methods=allmethods)
def createNewProductView():
    return render_template("addProduct.html")

@app.route("/deleteProduct", methods=allmethods)
def deleteAProduct():
    return render_template("deleteProduct.html")

@app.route("/stockForAProduct",methods=getMethod)
def stockProducts():
    return render_template("stockProducts.html")





