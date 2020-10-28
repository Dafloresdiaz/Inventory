from databaseConnection import connectionToDatabase as database
import sys

#Function to create the list of stores
def createListResults():
    conn = database()
    cursor = conn.cursor()
    resultsQuery = "SELECT P.NAME, P.TYPE_PRODUCT, S.NAME STORE, S.ADRESS, S.CITY, S.PHONE PRODUCT FROM PRODUCTS P INNER JOIN STORES S ON P.STORE_ID = S.STORE_ID"
    cursor.execute(resultsQuery)
    results = cursor.fetchall()
    return results
