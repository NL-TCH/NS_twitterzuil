from flask import Flask, redirect, url_for, render_template, request
from static import functions
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method =='POST':
        Titel = request.form['Titel']
        Klacht = request.form['Klacht']
        Titel = Titel.replace("'","''")
        Klacht = Klacht.replace("'","''")
        functions.moderator(Titel,Klacht)
        return render_template('bedankt.html')

    elif request.method =='GET':
        return render_template('index.html')

@app.route("/login", methods=["POST","GET"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/dashboard')
    return render_template('login.html', error=error)

@app.route("/dashboard",methods=["POST","GET"])
def dashboard():
    return render_template('dashboard.html')

@app.route("/moderator")
def moderator():
    return render_template('moderator.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)