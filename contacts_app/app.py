from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'contrasena_nueva'
app.config['MYSQL_HOST'] = 'contact_db'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contact_db (fullname, phone, email) VALUES (%s, %s, %s)', 
        (fullname, phone, email))
        mysql.connection.commit()
        return 'received ok'

@app.route('/edit_contact')
def edit_contact():
    return('edit')

@app.route('/delete')
def delete_contact():
    return('delete')

if __name__=='__main__':
    app.run(port = 3000, debug = True)