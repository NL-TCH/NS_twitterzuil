from flask import Flask, redirect, url_for, render_template, request, session
from turbo_flask import Turbo
turbo = Turbo()
import time, threading,sys,random

from static import functions
app = Flask(__name__)
turbo.init_app(app)

@app.route("/", methods=["POST", "GET"])
def klachten():
    if request.method =='POST':
        Naam = request.form['Name']
        if Naam =="":
            Naam='anoniem'
        Titel = request.form['Titel']
        Review = request.form['Review']
        Titel = Titel.replace("'","''")
        Naam = Naam.replace("'","''")
        Review = Review.replace("'","''")
        functions.moderator(Naam,Titel,Review)
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
            if functions.login(name,passw) =='false-credentials':
                return render_template('login.html', error='Onjuiste credentials')
            elif functions.login(name,passw) =='false-status':
                return render_template('login.html', error='Account inactief')
            elif functions.login(name,passw) =='true-status':
                session['logged_in'] = True
                session['gebruiker'] = name
                return redirect(url_for('dashboard'))
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
                return render_template('dashboard.html',naam= session['gebruiker'])
        if session['logged_in']:
            return render_template('dashboard.html',naam= session['gebruiker'])
        

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
                gegevens=functions.ophalen_moderatie()
                gegevens2 = functions.ophalen_moderated()
                if len(gegevens2)==0:
                    regels2 =0
                elif len(gegevens2)==1:
                    regels2 =1
                elif len(gegevens2)==2:
                    regels2 =2
                elif len(gegevens2)==3:
                    regels2 =3
                elif len(gegevens2)==4:
                    regels2 =4
                elif len(gegevens2)==5:
                    regels2 =5
                
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
                
                return render_template('moderatie.html', gegevens=functions.ophalen_moderatie(),gegevens2=functions.ophalen_moderated(),regels=regels, regels2=regels2,naam= session['gebruiker'])
        if session['logged_in']:
            gegevens=functions.ophalen_moderatie()
            gegevens2 = functions.ophalen_moderated()
            if len(gegevens2)==0:
                regels2 =0
            elif len(gegevens2)==1:
                regels2 =1
            elif len(gegevens2)==2:
                regels2 =2
            elif len(gegevens2)==3:
                regels2 =3
            elif len(gegevens2)==4:
                regels2 =4
            elif len(gegevens2)==5:
                regels2 =5
            
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
            
            return render_template('moderatie.html', gegevens=functions.ophalen_moderatie(),gegevens2=functions.ophalen_moderated(),regels=regels, regels2=regels2,naam= session['gebruiker'])
    

@app.route('/submit', methods=["POST","GET"])
def submit():
    if request.method == "POST":
        total=[]
        try:
            if request.form["Keuze1"] != None:
                Keuze1 = request.form["Keuze1"]
                total.append(Keuze1)
        except KeyError:
            print()
        try:
            if request.form["Keuze2"] != None:
                Keuze2 = request.form["Keuze2"]
                total.append(Keuze2)
        except KeyError:
            print()
        try:
            if request.form["Keuze3"] != None:
                Keuze3 = request.form["Keuze3"]
                total.append(Keuze3)
        except KeyError:
            print()
        try:
            if request.form["Keuze4"] != None:
                Keuze4 = request.form["Keuze4"]
                total.append(Keuze4)
        except KeyError:
            print()
        try:
            if request.form["Keuze5"] != None:
                Keuze5 = request.form["Keuze5"]
                total.append(Keuze5)
        except KeyError:
            print()
        functions.moderatie_toepassen(total,user=session['gebruiker'])
        return redirect(url_for('moderator'))

@app.route("/statistieken/woordenfiltering",methods=['GET', 'POST'])
def woordenfiltering():
    """ Session control"""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if session['logged_in']:
                gegevens=functions.woordenfiltering_ophalen()
                gegevens2=functions.statistieken_ophalen()
                return render_template('woordenfiltering_statistics.html',gegevens=gegevens,gegevens2=gegevens2,naam= session['gebruiker'])
        if session['logged_in']:
            gegevens=functions.woordenfiltering_ophalen()
            gegevens2=functions.statistieken_ophalen()
            return render_template('woordenfiltering_statistics.html',gegevens=gegevens,gegevens2=gegevens2,naam= session['gebruiker'])

@app.route("/statistieken/gebruikers",methods=['GET', 'POST'])
def gebruikers():
    """ Session control"""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if session['logged_in']:
                gegevens=functions.gebruikers_statistieken_ophalen()
                return render_template('gebruikers_statistics.html',gegevens=gegevens,naam= session['gebruiker'])
        if session['logged_in']:
            gegevens=functions.gebruikers_statistieken_ophalen()
            return render_template('gebruikers_statistics.html',gegevens=gegevens,naam= session['gebruiker'])

@app.route("/voorkeuren/bot",methods=['GET', 'POST'])
def voorkeuren():
    """ Session control"""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
        
            if session['logged_in']:
                print(request.form)
                if request.form['toevoegen/verwijderen'] =='toevoegen':
                    scheldwoord=request.form["filterwoord"]
                    functions.filterwoorden_toevoegen(scheldwoord.lower())
                elif request.form['toevoegen/verwijderen'] == 'verwijderen':
                    scheldwoord=request.form["category"]
                    functions.filterwoorden_verwijderen(scheldwoord.lower())
                # gegevens=functions.ophalen_voorkeuren()
                # return render_template('voorkeuren.html',gegevens=gegevens)
                return redirect(url_for('voorkeuren',naam= session['gebruiker']))
        if session['logged_in']:
            gegevens=functions.ophalen_voorkeuren()
            return render_template('voorkeuren.html',gegevens=gegevens,naam= session['gebruiker'])

@app.route("/voorkeuren/gebruikers",methods=['GET', 'POST'])
def voorkeuren_gebruikers():
    """ Session control"""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
        
            if session['logged_in']:
                print(request.form)
                if request.form['toevoegen/verwijderen'] =='toevoegen':
                    gebruikersnaam=request.form["gebruikersnaam"]
                    wachtwoord=request.form["wachtwoord"]
                    functions.gebruikers_toevoegen(gebruikersnaam,wachtwoord)
                elif request.form['toevoegen/verwijderen'] == 'verwijderen':
                    gebruikersnaam=request.form["category1"]
                    functions.gebruikers_verwijderen(gebruikersnaam)
                elif request.form['toevoegen/verwijderen'] == 'wijzigen':
                    gebruikersnaam=request.form["category2"]
                    functions.gebruikers_wijzigen(gebruikersnaam)
                return redirect(url_for('voorkeuren_gebruikers',naam= session['gebruiker']))
        if session['logged_in']:
            gegevens=functions.ophalen_gebruikers()
            return render_template('voorkeuren gebruikers.html',gegevens=gegevens,naam= session['gebruiker'])


@app.route("/twitter", methods=['GET', 'POST'])
def twitter():
    return render_template('twitterboard.html')


@app.context_processor
def inject_load():
    tweets=functions.tweets_ophalen()
    tijd=functions.check_timestamp()
    return {'var1': tweets[:], 'var2':tijd}

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

def update_load():
    with app.app_context():
        while True:
            time.sleep(10)
            turbo.push(turbo.replace(render_template('tweets.html'), 'load'))
       
if __name__ == "__main__":
    app.secret_key = "123"
    app.run(debug=True,host='0.0.0.0',port=8085)