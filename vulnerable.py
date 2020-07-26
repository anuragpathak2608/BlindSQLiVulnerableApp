# Sample app that's vulnerable to boolean blind SQL injection. 
from flask import Flask, abort
from flask_mysqldb import MySQL
import json

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'baba'

mysql = MySQL(app)

@app.route('/users/<userId>', methods=['GET'])
def getUsers(userId): 
    returnString = ''
    try:
        cur = mysql.connection.cursor()
        queryString = "SELECT * FROM users WHERE id = {0}".format(userId)
        print queryString
        cur.execute(queryString)
        rowHeaders=[x[0] for x in cur.description]
        data = cur.fetchall()
        jsonData=[]
        for result in data:
            jsonData.append(dict(zip(rowHeaders,result)))
        
        print jsonData
        cur.close()
        
        for item in jsonData:
             returnString += "FOUND "

        return returnString

    except Exception as e:
        #returnString = "Oops! This is not your chosen path"
        abort(500)

    # finally:
    #     return returnString


@app.errorhandler(500)
def internal_error(error):
    return "Mayday! Mayday! <br><br>CODE 500! <br><br>I repeat... <br><br> <h1> CODE 500! </h1>"

@app.errorhandler(404)
def not_found(error):
    return "You seem to have lost your way !"

if __name__ == '__main__':
    app.run()