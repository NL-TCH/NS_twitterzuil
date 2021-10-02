import psycopg2 as sql

conn = sql.connect('host=127.0.0.1 user=NS_User password=NS_Password dbname=NS_Database')
cursor = conn.cursor()

def moderator(Titel, Klacht):
    cursor.execute('SELECT woorden FROM Moderatie')
    Titel_split = Titel.split(' ')
    Klacht_split = Klacht.split(' ')
    records = cursor.fetchall()
    Titel_status = None
    Klacht_status = None
    for rows in records:
        clean = ''.join(rows)
        for words in Titel_split:
            if words == clean:
                Titel_status= False
                cursor.execute(f'''UPDATE moderatie set frequentie = frequentie +1 where woorden = '{clean}' ''')
                conn.commit()
                Scheldwoord=clean
                print(f'>>Titel>>{words} is equal to {clean}')
        for words in Klacht_split:
            if words == clean:
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
        cursor.execute(f'''INSERT INTO klachten (titel,klacht,scheldwoord,status) VALUES ('{Titel}','{Klacht}','{Scheldwoord}', 0);''')
        conn.commit()
    elif Titel_status != False and Klacht_status != False:
        cursor.execute(f'''INSERT INTO klachten (titel,klacht,status) VALUES ('{Titel}','{Klacht}', 1);''')
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
    gegevens =cursor.fetchall() #
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
