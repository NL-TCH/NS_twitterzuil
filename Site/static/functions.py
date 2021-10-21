import psycopg2 as sql
import psycopg2.extras

conn = sql.connect('host=192.168.1.52 user=NS_User password=NS_Password dbname=NS_Database')
cursor = conn.cursor()

def moderator(Naam,Titel, Klacht):
    cursor.execute('SELECT woorden FROM Moderatie')
    Titel_split = Titel.split(' ')
    Klacht_split = Klacht.split(' ')
    records = cursor.fetchall()
    Titel_status = None
    Klacht_status = None
    for rows in records:
        clean = ''.join(rows)
        for words in Titel_split:
            print(words.lower())
            print(clean)
            if words.lower() == clean:
                Titel_status= False
                cursor.execute(f'''UPDATE moderatie set frequentie = frequentie +1 where woorden = '{clean}' ''')
                conn.commit()
                Scheldwoord=clean
                print(f'>>Titel>>{words} is equal to {clean}')
        for words in Klacht_split:
            print(words.lower())
            if words.lower() == clean:
                Klacht_status= False
                Scheldwoord=clean
                cursor.execute(f'''UPDATE moderatie set frequentie = frequentie +1 where woorden = '{clean}' ''')
                conn.commit()
                print(f'>>Klacht>>{words} is equal to {clean}')
    #bot, scheldwoord = 0
    #clean, nieuw = 1
    #clean, geaccepteerd = 2
    #clean, niet geaccepteerd = 3
    if Titel_status == False or Klacht_status == False:
        cursor.execute(f'''INSERT INTO klachten (naam,titel,klacht,scheldwoord,status) VALUES ('{Naam}','{Titel}','{Klacht}','{Scheldwoord}', 0);''')
        conn.commit()
    elif Titel_status != False and Klacht_status != False:
        cursor.execute(f'''INSERT INTO klachten (naam,titel,klacht,status) VALUES ('{Naam}','{Titel}','{Klacht}', 1);''')
        conn.commit()
    else:
        print('error')

def ophalen_moderatie():
    cursor.execute(f'''SELECT titel, klacht FROM klachten where status = '1' ORDER BY id limit 5''')
    conn.commit()
    gegevens = cursor.fetchall()
    titels = [x[0] for x in gegevens]
    klachten = [x[1] for x in gegevens]
    combinatie = [list(a) for a in zip(titels, klachten)]
    return combinatie

def ophalen_moderated():
    cursor.execute(f'''SELECT titel, klacht, scheldwoord, status FROM klachten where status NOT IN ('1') ORDER BY id DESC limit 5''')
    conn.commit()
    gegevens =cursor.fetchall()
    titels = [x[0] for x in gegevens]
    klachten = [x[1] for x in gegevens]
    scheldwoorden = [x[2] for x in gegevens]
    status = [x[3] for x in gegevens]
    combinatie = [list(a) for a in zip(titels,klachten,scheldwoorden,status)]
    return combinatie

def moderatie_toepassen(total):
    for keuze in total:
        #2.0
        if (int(keuze.replace('.',''))% 2) == 0:
            cursor.execute(f''' UPDATE klachten
                                SET status = 3
                                WHERE id IN (SELECT id
                                FROM klachten
                                WHERE status =1
                                ORDER BY id
                                LIMIT 1);''')
            conn.commit()
        #2.1
        elif ((int(keuze.replace('.',''))% 2) == 0) ==False:
            cursor.execute(f''' UPDATE klachten
                                SET status = 2
                                WHERE id IN (SELECT id
                                FROM klachten
                                WHERE status =1
                                ORDER BY id
                                LIMIT 1);''')
            conn.commit()

def woordenfiltering_ophalen():
    cursor.execute(f'''select * from moderatie ORDER BY frequentie DESC limit 5''')
    conn.commit()
    gegevens =cursor.fetchall()
    woorden = [x[0] for x in gegevens]
    frequentie = [x[1] for x in gegevens]
    combinatie = [list(a) for a in zip(woorden,frequentie)]
    return combinatie


def ophalen_voorkeuren():
    cursor.execute(f'''select * from moderatie ORDER BY frequentie DESC''')
    conn.commit()
    gegevens =cursor.fetchall()
    woorden = [x[0] for x in gegevens]
    frequentie = [x[1] for x in gegevens]
    combinatie = [list(a) for a in zip(woorden,frequentie)]
    return combinatie

def filterwoorden_toevoegen(woord):
    cursor.execute(f'''insert into moderatie (woorden,frequentie) VALUES ('{woord}','0');''')
    conn.commit()

def filterwoorden_verwijderen(woord):
    cursor.execute(f'''delete from moderatie where woorden='{woord}';''')
    conn.commit()

def statistieken_ophalen():
    cursor.execute(f'''select status from klachten where status = 0''')
    conn.commit()
    gegevens0 =cursor.fetchall()
    status0=len(gegevens0)
    cursor.execute(f'''select status from klachten where status = 1''')
    conn.commit()
    gegevens1 =cursor.fetchall()
    status1=len(gegevens1)
    cursor.execute(f'''select status from klachten where status = 2''')
    conn.commit()
    gegevens2 =cursor.fetchall()
    status2=len(gegevens2)
    cursor.execute(f'''select status from klachten where status = 3''')
    conn.commit()
    gegevens3 =cursor.fetchall()
    status3=len(gegevens3)
    status =[status0,status1,status2,status3]
    return status

def tweets_ophalen():
    #cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute(f'''SELECT naam, titel, klacht FROM klachten where status = '2' ORDER BY id desc limit 6''')
    conn.commit()

    tweets = cursor.fetchall()
    naam = [x[0] for x in tweets]
    titel = [x[1] for x in tweets]
    klacht = [x[2] for x in tweets]
    tweet_list = [list(a) for a in zip(naam,titel,klacht)]
    return tweet_list

statistieken_ophalen()