import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import time

@app.route("/USERS")
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT , FIRST_NAME, NAME, EMAIL, PASSWORD FROM USER")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/LOGINFO", methods=['POST', 'GET'])
def emp_log():
    EMAIL="null"
    PASSWORD="null"
    if request.method == 'POST':
        EMAIL = request.form['EMAIL']
        PASSWORD = request.form['PASSWORD']
        app.logger.info("%s , %s", EMAIL ,PASSWORD)
        print(request)
      
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "SELECT ID, FIRST_NAME, NAME, EMAIL, PASSWORD, SACODE FROM USER WHERE EMAIL=%s AND PASSWORD=%s"
        sqlQuery = "SELECT ID, FIRST_NAME, USER.NAME, EMAIL, PASSWORD, USER.SACODE, WGGBS, WGNAME FROM USER INNER JOIN SHAREDAPPARTMENT ON USER.SACODE = SHAREDAPPARTMENT.SACODE WHERE USER.EMAIL=%s AND USER.PASSWORD=%s;"
        bindData = (EMAIL, PASSWORD)  
        cursor.execute(sqlQuery, bindData)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/WGBS", methods=['POST', 'GET'])
def emp_wgbs():
    SACODE="null"
    if request.method == 'POST':
        SACODE = request.form['SACODE']
        app.logger.info("%s", SACODE )
        print(request)
      
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "SELECT WGGBS, WGNAME FROM SHAREDAPPARTMENT WHERE SACODE=%s"
        bindData = (SACODE)  
        cursor.execute(sqlQuery, bindData)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/NEWUSER", methods=['POST'])
def emp_create():
    EMAIL="null"
    PASSWORD="null"
    if request.method == 'POST':
        FIRST_NAME = request.form['FIRST_NAME']
        NAME = request.form['NAME']
        EMAIL = request.form['EMAIL']
        PASSWORD = request.form['PASSWORD']
        SACODE = request.form['SACode']
        app.logger.info("%s , %s, %s, %s, %s", FIRST_NAME ,NAME, EMAIL, PASSWORD, SACODE)
        print(request)

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "INSERT INTO USER(ID, FIRST_NAME, NAME, EMAIL, PASSWORD, SACODE) VALUES(NULL ,%s, %s, %s, %s, %s)"
        bindData = (FIRST_NAME, NAME, EMAIL, PASSWORD, SACODE) 
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("Added new User !")
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/NEWHIGHSCORE", methods=['POST'])
def emp_createHighscore():
    USERID = "null"
    SACODE = "null"
    DATE= "null"
    ROOM = "null"
    FIRST_NAME = "null"
    NAME = "null"

    if request.method == 'POST':
        USERID = request.form['USERID']
        SACODE = request.form['SACODE']
        DATE = request.form['DATE']
        ROOM = request.form['ROOM']
        app.logger.info("%s , %s, %s, %s", FIRST_NAME ,NAME, DATE, USERID, SACODE, ROOM)
        print(request)

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "INSERT INTO HIGHSCORE(IDHIGHSCORE, USERID, SACODE, DATE, ROOM) VALUES(NULL ,%s, %s, %s, %s)"
        bindData = (USERID, SACODE, DATE, ROOM) 
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("Added new Highscore !")
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/GETHIGHSCORESOFWG", methods=['POST', 'GET'])
def emp_getHighscores():
    SACODE = "null"
    ROOM = "null"
    if request.method == 'POST':
        SACODE = request.form['SACODE']
        ROOM = request.form['ROOM']
        DATEFORMAT = "%d/%m/%Y %H:%i"
        app.logger.info("%s , %s", ROOM ,SACODE)
        print(request)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "SELECT IDHIGHSCORE, USERID, USER.SACODE, DATE_FORMAT(DATE, %s) AS DATE, HIGHSCORE.ROOM, FIRST_NAME, NAME FROM HIGHSCORE INNER JOIN USER ON HIGHSCORE.USERID = USER.ID WHERE USER.SACODE=%s and HIGHSCORE.ROOM=%s"
        bindData = (DATEFORMAT,SACODE, ROOM)  
        cursor.execute(sqlQuery, bindData)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        print(response)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/GETSHOPPINGLISTSFROMUSER", methods=['POST', 'GET'])
def emp_getShoppingLists():
    AUTHORID = "null"
    if request.method == 'POST':
        AUTHORID = request.form['AUTHORID']
        app.logger.info("%s: AUHTORID for whom a shopping lists shall be fetched", AUTHORID)
        print(request)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "SELECT SHOPPING_LIST.ID, SHOPPING_LIST.TITLE, USER.FIRST_NAME, SHOPPING_LIST.LAST_EDITED FROM SHOPPING_LIST JOIN USER WHERE SHOPPING_LIST.AUTHOR=%s AND USER.ID=%s"
        bindData = (AUTHORID, AUTHORID)  
        cursor.execute(sqlQuery, bindData)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        print(response)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/CREATESHOPPINGLISTFROMUSER", methods=['POST', 'GET'])
def emp_createShoppingList():
    AUTHORID = "null"
    if request.method == 'POST':
        AUTHORID = request.form['AUTHORID']
        app.logger.info("%s: AUTHORID for which a shopping list shall be created", AUTHORID)
        print(request)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "INSERT INTO SHOPPING_LIST (ID, TITLE, LAST_EDITED, AUTHOR) VALUES (null, 'New Shopping List', DEFAULT, %s)"
        bindData = (AUTHORID)  
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("NEW SHOPPING_LIST CREATED")
        print(response)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/UPDATESHOPPINGLISTFROMUSER", methods=['PUT', 'GET'])
def emp_updateShoppingListFromUser():
    AUTHORID = "null"
    SHOPPINGLISTID = "null"
    newTITLE = "null"
    if request.method == 'PUT':
        AUTHORID = request.form['AUTHORID']
        SHOPPINGLISTID = request.form['SHOPPINGLISTID']
        newTITLE = request.form['newTITLE']
        app.logger.info("AUTHORID: %s, SHOPPINGLISTID: %s, newTITLE: %s", AUTHORID, SHOPPINGLISTID, newTITLE)
        print(request)
      
    try:
        sqlQuery = "UPDATE SHOPPING_LIST SET TITLE = %s, LAST_EDITED = DEFAULT WHERE AUTHOR = %s AND ID = %s"
        bindData = (newTITLE, AUTHORID, SHOPPINGLISTID)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("UPDATED SHOPPING LIST TITLE!")
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/DELETESHOPPINGLISTFROMUSER", methods=['DELETE'])
def emp_deleteShoppingLists():
    if request.method == 'DELETE':
        AUTHORID = request.form['AUTHORID']
        SHOPPINGLISTID = request.form['SHOPPINGLISTID']
        app.logger.info("%s; %s: AUTHORID & SHOPPINGLISTID which shall be deleted", AUTHORID, SHOPPINGLISTID)
        print(request)
    try:
        sqlQuery = "DELETE FROM SHOPPING_LIST WHERE AUTHOR=%s AND ID=%s"
        bindData = (AUTHORID, SHOPPINGLISTID)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("DELETED SHOPPING_LIST")
        response.status_code = 200
        print(response)
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/GETSHOPPINGLISTITEMS", methods=['POST', 'GET'])
def emp_getShoppingListItems():
    SHOPPINGLISTID = "null"
    if request.method == 'POST':
        SHOPPINGLISTID = request.form['SHOPPINGLISTID']
        app.logger.info("%s: SHOPPINGLISTID for which Shopping List Items shall be fetched", SHOPPINGLISTID)
        print(request)
    try:
        sqlQuery = "SELECT * FROM SHOPPING_LIST_ITEM WHERE SHOPPING_LIST=%s"
        bindData = (SHOPPINGLISTID)  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        print(response)
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/CREATESHOPPINGLISTITEM", methods=['POST', 'GET'])
def emp_createShoppingListItem():
    SHOPPINGLISTID = "null"
    if request.method == 'POST':
        SHOPPINGLISTID = request.form['SHOPPINGLISTID']
        app.logger.info("%s: SHOPPINGLISTID for which a shopping list item shall be created", SHOPPINGLISTID)
        print(request)
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "INSERT INTO SHOPPING_LIST_ITEM (ID, TITLE, AMOUNT, UNIT, SHOPPING_LIST) VALUES (null, 'new item', 0, DEFAULT, %s)"
        bindData = (SHOPPINGLISTID)  
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("NEW SHOPPING_LIST_ITEM CREATED")
        print("SHOPPING LIST ITEM CREATED")
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/UPDATESHOPPINGLISTITEM", methods=['PUT', 'GET'])
def emp_updateShoppingListItem():
    ID = "null"
    newTITLE = "null"
    newAMOUNT = "null"
    newUNIT = "null"
    if request.method == 'PUT':
        ID = request.form['ID']
        newTITLE = request.form['newTITLE']
        newAMOUNT = request.form['newAMOUNT']
        newUNIT = request.form['newUNIT']
        app.logger.info("ID: %s, newTITLE: %s, newAMOUNT: %s, newUNIT: %s", ID, newTITLE, newAMOUNT, newUNIT)
        print(request)
      
    try:
        sqlQuery = "UPDATE SHOPPING_LIST_ITEM SET TITLE = %s, AMOUNT = %s, UNIT=%s WHERE ID = %s"
        bindData = (newTITLE, newAMOUNT, newUNIT, ID)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("UPDATED SHOPPING LIST ITEM!")
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/DELETESHOPPINGLISTITEM", methods=['DELETE'])
def emp_deleteShoppingListItem():
    SHOPPINGLISTITEMID = "null"
    if request.method == 'DELETE':
        SHOPPINGLISTITEMID = request.form['SHOPPINGLISTITEMID']
        app.logger.info("%s: SHOPPINGLISTITEMID which shall be deleted", SHOPPINGLISTITEMID)
        print(request)
    try:
        sqlQuery = "DELETE FROM SHOPPING_LIST_ITEM WHERE ID=%s"
        bindData = (SHOPPINGLISTITEMID)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("DELETED SHOPPING_LIST_ITEM")
        response.status_code = 200
        print(response)
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/UPDATETOILETSTATUS", methods=['PUT', 'GET'])
def emp_updateToiletStatus():
    SACODE="null"

    if request.method == 'PUT':
        SACODE = request.form['SACODE']
        app.logger.info("SACODE : %s", SACODE)
        print(request)
      
    try:
        sqlQuery = "UPDATE SHAREDAPPARTMENT SET isToilet = IF(isToilet='1', '0', '1') WHERE SACODE=%s"
        bindData = (SACODE)  
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("UPDATED isToilet")
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/GETTOILETSTATUS", methods=['POST', 'GET'])
def emp_getToiletStatus():
    SACODE="null"
    if request.method == 'POST':
        SACODE = request.form['SACODE']
        app.logger.info("%s", SACODE)
        print(request)
      
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "SELECT isToilet FROM SHAREDAPPARTMENT WHERE SACODE=%s"
        bindData = (SACODE)  
        cursor.execute(sqlQuery, bindData)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/UPDATESETTINGS", methods=['PUT', 'GET'])
def emp_updateSettings():
    oldSACODE="null"
    newSACODE="null"
    newEMAIL="null"
    newPASSWORD="null"
    oldEMAIL="null"
    oldPASSWORD="null"

    if request.method == 'PUT':
        oldSACODE = request.form['oldSACODE']
        newSACODE = request.form['newSACODE']
        oldEMAIL = request.form['oldEMAIL']
        newEMAIL = request.form['newEMAIL']
        newPASSWORD = request.form['newPASSWORD']
        oldPASSWORD = request.form['oldPASSWORD']
        app.logger.info("oldSACODE : %s, newSACODE: %s, oldEMAIL : %s, newEMAIL : %s, oldPASSWORD : %s, newPASSWORD : %s", oldSACODE, newSACODE, oldEMAIL, newEMAIL, oldPASSWORD, newPASSWORD)
        print(request)
      
    try:
        sqlQuery = "UPDATE USER USER INNER JOIN SHAREDAPPARTMENT ON USER.SACODE = SHAREDAPPARTMENT.SACODE SET USER.SACODE=%s, USER.EMAIL=%s, USER.PASSWORD=%s WHERE USER.EMAIL=%s AND USER.PASSWORD=%s AND USER.SACODE=%s"
        bindData = (newSACODE, newEMAIL, newPASSWORD, oldEMAIL, oldPASSWORD, oldSACODE)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("UPDATED USER SACODE, EMAIL, PASSWORD")
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/UPDATEWGBS", methods=['PUT', 'GET'])
def emp_updateWGBS():
    oldWGBs="null"
    SACode="null"
    newWGBs="null"

    if request.method == 'PUT':
        oldWGBs = request.form['oldWGBs']
        newWGBs = request.form['newWGBs']
        oldTitle = request.form['oldTitle']
        newTitle = request.form['newTitle']
        SACode = request.form['SACode']
        app.logger.info("oldWGBs : %s, newWGBs : %s, SACode : %s, oldTitle : %s, newTitle : %s", oldWGBs, newWGBs, SACode,oldTitle,newTitle)
        print(request)
    try:
        sqlQuery = "UPDATE SHAREDAPPARTMENT SET WGGBS=%s, WGNAME=%s WHERE WGGBS=%s AND SACODE=%s"
        bindData = (newWGBs,newTitle, oldWGBs, SACode)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        empRows = cursor.fetchall()
        response = jsonify("UPDATED WGBS")
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        "status": 404,
        "message": "Record not found: " + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run(debug=True)
