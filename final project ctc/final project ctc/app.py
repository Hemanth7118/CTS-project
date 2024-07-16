from flask import Flask, request, render_template,redirect,url_for
from datetime import datetime, date
import math
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="root123",
  database="sample"
)


# @app.route('/record')
# def record():
#     cursor = mydb.cursor()
#     sql = "SELECT * FROM details ORDER BY user_name ASC"
#     cursor.execute(sql)
#     records = cursor.fetchall()

#     return render_template('record.html', records=records)


@app.route('/', methods=['GET','POST'])
def user_details():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password = request.form.get('password')
        # date= datetime.datetime.now()
        date=datetime.today()
    
        cursor = mydb.cursor()
        sql = "INSERT INTO details (user_id, user_name, email, password, created_date) VALUES (%s, %s, %s, %s, %s)"
        val = (user_id, user_name, email, password, date)
        cursor.execute(sql, val)
        mydb.commit()

    return render_template('registration (2).html')


@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')

        cursor = mydb.cursor()
        sql = "SELECT * FROM details WHERE user_id = %s AND password = %s "
        val = (user_id, password)
        cursor.execute(sql, val)
        user = cursor.fetchone()

        if user:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('unsuccess'))


    return render_template('login (2).html')
@app.route('/forgot_password', methods=['GET','POST'])
def forgot_password():
    if request.method == 'POST':
        user_id= request.form.get('user_id')
        new_password = request.form.get('new_password')
        cursor = mydb.cursor()
        sql = "UPDATE details SET password = %s WHERE user_id =%s "
        val = (new_password, user_id)
        cursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('login (2)'))

    return render_template('forgot_password.html')
@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/unsuccess (1)')
def unsuccess():
    return render_template('unsuccess (1).html')



if __name__ == '__main__':
    app.run(debug=True)