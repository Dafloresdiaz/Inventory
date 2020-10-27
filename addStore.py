from databaseConnection import connectionToDatabase as database

#Function to insert a new Store
def addNewStore(storeName):
    isInserted = False
    if storeName:
        conn = database()
        cursor = conn.cursor()
        checkQuery = "SELECT STORE_ID FROM STORES WHERE NAME='{0}'".format(storeName)
        cursor.execute(checkQuery)
        if cursor.fetchone() is None:
            insertQuery="INSERT INTO STORES(NAME) VALUES('{0}')".format(storeName)
            cursor.execute(insertQuery)
            conn.commit()
            isInserted = True
        conn.close()
        return isInserted
    else:
        return isInserted
