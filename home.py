from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app = Flask(__name__)

con=sqlite3.connect('database.db')
try:
    con.execute("Create TABLE  users (name TEXT,age INTEGER)")
except:
    pass
    

@app.route('/')
def fun1():
    return "welcome"

@app.route('/fun2')
def fun2():
    return "sample fun"

@app.route('/index',methods=['POST','GET'])
def fun3():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        con =sqlite3.connect('database.db')
        con.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        con.commit()
        print(name,age)
        return redirect(url_for('fun3'))
    else:
        con=sqlite3.connect('database.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall() 
        return render_template('index.html',users=users)

app.run()