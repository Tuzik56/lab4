from flask import Flask, render_template, request, abort
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db", user="postgres", password="sysiskakolbosa", host="localhost", port="5432")
cursor = conn.cursor()


@app.route('/login', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(login), str(password)))
    records = list(cursor.fetchall())

    if login and password and records:
        return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
    else:
        abort(404, "Что-то не так")


app.run()
