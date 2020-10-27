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

#Function to add/insert a new inventory
#The will need to fill the name and also provide to which store will be related
def addNewInventory(inventoryName, store):
    isInserted = False
    if inventoryName and store:
        conn = database()
        cursor = conn.cursor()
        storeQuery = "SELECT STORE_ID FROM STORES WHERE NAME = '{0}'". format(store)
        cursor.execute(storeQuery)
        storeID = cursor.fetchone()[0]
        checkQuery = "SELECT INVENTORY_ID FROM INVENTORIES WHERE NAME='{0}' AND STORE_ID={1}".format(inventoryName, storeID)
        cursor.execute(checkQuery)
        if cursor.fetchone() is None:
            insertQuery = "INSERT INTO INVENTORIES(NAME, STORE_ID) VALUES('{0}',{1})".format(inventoryName,storeID)
            cursor.execute(insertQuery)
            conn.commit()
            isInserted = True
        conn.close()
        return isInserted
    else:
        return isInserted



