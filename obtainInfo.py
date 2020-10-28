from databaseConnection import connectionToDatabase as database
import psycopg2
import psycopg2.extras
import sys

#Function to create the list of stores
def createListResults():
    conn = database()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    resultsQuery = "SELECT P.NAME PRODUCT, P.TYPE_PRODUCT, S.NAME STORE, S.ADRESS, S.CITY, S.PHONE FROM PRODUCTS P INNER JOIN STORES S ON P.STORE_ID = S.STORE_ID"
    cursor.execute(resultsQuery)
    results = cursor.fetchall()
    result1 = []
    for col in results:
        result1.append(dict(col))
    return result1

#Create a function to handle more filters to the data
def filterListResults(store, product, typeProd, city):
    conn = database()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "SELECT P.NAME PRODUCT, P.TYPE_PRODUCT, S.NAME STORE, S.ADRESS, S.CITY, S.PHONE FROM PRODUCTS P INNER JOIN STORES S ON P.STORE_ID = S.STORE_ID WHERE"
    filters = []
    #check each filter
    if store:
        query += " S.NAME='{0}' AND".format(store)
        filters.append(store)
    if product:
        query += " P.NAME='{0}' AND".format(product)
        filters.append(product)
    if typeProd:
        query += " P.TYPE_PRODUCT='{0}' AND".format(typeProd)
        filters.append(typeProd)
    if city:
        query += " S.CITY='{0}' AND".format(city)
        filters.append(city)

    query = query[:-4]
    cursor.execute(query)
    results = cursor.fetchall()
    result1 = []
    for col in results:
        result1.append(dict(col))
    return result1


