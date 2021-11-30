from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)

output = {}
table = 'techincalhomeschool'

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('Registrationform.html')
	
	@app.route("/addenquiry", methods=['POST'])
def technical():

	name = request.form['name']
    email = request.form['email']
    cont_no = request.form['cont_no']
    course = request.form['course']
	
	insert_sql = "INSERT INTO techincalhomeschool VALUES (%s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if 
        cursor.execute(insert_sql, (name , email , cont_no ,Details ))
        db_conn.commit()
        name = "" + email + " " + cont_no + " "Details
    
        try:
            print("Data inserted in MySQL RDS... ")
           

        except Exception as e:
            return str(e)

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('Output.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)