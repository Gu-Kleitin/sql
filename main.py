from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cadastro_clientes'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', clientes=data)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clientes (nome, email) VALUES (%s, %s)', (nome, email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
