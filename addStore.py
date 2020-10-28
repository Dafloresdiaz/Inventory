from databaseConnection import connectionToDatabase as database

#Function to insert a new Store
def addNewStore(storeName, adress, city, phoneNumber):
    isInserted = False
    if storeName and adress and city and phoneNumber:
        conn = database()
        cursor = conn.cursor()
        cursorSc = conn.cursor()
        checkNameQuery = "SELECT STORE_ID FROM STORES WHERE NAME='{0}'".format(storeName)
        checkAdressQuery = "SELECT STORE_ID FROM STORES WHERE ADRESS='{0}'".format(adress)
        cursor.execute(checkNameQuery)
        cursorSc.execute(checkAdressQuery)
        if cursor.fetchone() is None and cursorSc.fetchone() is None:
            insertQuery="INSERT INTO STORES(NAME, ADRESS, CITY, PHONE) VALUES('{0}', '{1}', '{2}', '{3}')".format(storeName, adress, city, phoneNumber)
            cursor.execute(insertQuery)
            conn.commit()
            isInserted = True
        conn.close()
        return isInserted
    else:
        return isInserted
