from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL()

@app.route('/')
def index():
    return('Hola')

@app.route('/add_contact')
def add_contact():
    return('add')

@app.route('/edit_contact')
def edit_contact():
    return('edit')

@app.route('/delete')
def delete_contact():
    return('delete')

if __name__=='__main__':
    app.run(port = 3000, debug = True)