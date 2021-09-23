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
    #scheldwoord = 0
    #clean, niet geaccepteerd = 1
    #clean, geaccepteerd = 2
    if Titel_status == False or Klacht_status == False:
        cursor.execute(f'''INSERT INTO klachten (titel,klacht,scheldwoord,status) VALUES ('{Titel}','{Klacht}','{Scheldwoord}', 0);''')
        conn.commit()
    elif Titel_status != False and Klacht_status != False:
        cursor.execute(f'''INSERT INTO klachten (titel,klacht,status) VALUES ('{Titel}','{Klacht}', 1);''')
        conn.commit()
    else:
        print('error')

def ophalen_gegevens():
    cursor.execute(f'''SELECT titel, klacht FROM klachten where status = '1' limit 5''')
    conn.commit()
    gegevens = cursor.fetchall()
    titels = [x[0] for x in gegevens]
    klachten = [x[1] for x in gegevens]
    combinatie = [list(a) for a in zip(titels, klachten)]
    return combinatie