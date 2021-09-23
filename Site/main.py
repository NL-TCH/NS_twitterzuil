from flask import Flask, redirect, url_for, render_template, request, session
from static import functions
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def klachten():
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
    """Login Form"""
    
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            if name == 'admin' and passw == 'admin':
                session['logged_in'] = True
                return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', error='Onjuiste credentials')
        except:
            return render_template('login.html', error='Onjuiste credentials')
        


@app.route("/dashboard",methods=["POST","GET"])
def dashboard():
    """ Session control"""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if session['logged_in']:
                return render_template('dashboard.html')
        if session['logged_in']:
            return render_template('dashboard.html')
        

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('login'))
    
@app.route("/moderatie")
def moderator():
    """ Session control"""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if session['logged_in']:
                gegevens=functions.ophalen_gegevens()
                if len(gegevens)==0:
                    regels =0
                elif len(gegevens)==1:
                    regels =1
                elif len(gegevens)==2:
                    regels =2
                elif len(gegevens)==3:
                    regels =3
                elif len(gegevens)==4:
                    regels =4
                elif len(gegevens)==5:
                    regels =5
                
                return render_template('moderatie.html', gegevens=functions.ophalen_gegevens(),regels=regels)
        if session['logged_in']:
            gegevens=functions.ophalen_gegevens()
            if len(gegevens)==0:
                regels =0
            elif len(gegevens)==1:
                regels =1
            elif len(gegevens)==2:
                regels =2
            elif len(gegevens)==3:
                regels =3
            elif len(gegevens)==4:
                regels =4
            elif len(gegevens)==5:
                regels =5
            
            return render_template('moderatie.html', gegevens=functions.ophalen_gegevens(),regels=regels)
    

if __name__ == "__main__":
    app.secret_key = "123"
    app.run(debug=True,host='0.0.0.0',port=8080)