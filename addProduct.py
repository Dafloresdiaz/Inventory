from databaseConnection import connectionToDatabase as database
import sys

#Function to create the list of stores
def createListStores():
    conn = database()
    cursor = conn.cursor()
    storesQuery = "SELECT NAME FROM STORES"
    cursor.execute(storesQuery)
    #Create a list comprehenssion to have the correct format for the list
    listOfStores = [store[0] for store in cursor.fetchall()]
    return listOfStores

#Function to add/insert a new prodcut
#The will need to fill the name and also provide to which store will be related
def addNewProduct(productName, typeProduct, storeSelection):
    isInserted = False
    if productName and typeProduct and storeSelection:
        conn = database()
        cursor = conn.cursor()
        storeQuery = "SELECT STORE_ID FROM STORES WHERE NAME = '{0}'".format(storeSelection)
        cursor.execute(storeQuery)
        storeID = cursor.fetchone()[0]
        #checkQuery = "SELECT PRODUCT_ID FROM PRODUCTS WHERE NAME ='{0}' AND STORE_ID={1}".format(productName, storeID)
        #cursor.execute(checkQuery)
        insertQuery = "INSERT INTO PRODUCTS(NAME, TYPE_PRODUCT, STORE_ID) VALUES('{0}', '{1}', {2})".format(productName, typeProduct, storeID)
        cursor.execute(insertQuery)
        conn.commit()
        isInserted = True
        conn.close()
        return isInserted
    else:
        return isInserted
