import psycopg2 as sql

conn = sql.connect('host=127.0.0.1 user=NS_User password=NS_Password dbname=NS_Database')
cursor = conn.cursor()

def moderator(Titel, Klacht):
    cursor.execute('SELECT * FROM Moderatie')
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
                print(f'>>Titel>>{words} is equal to {clean}')
        for words in Klacht_split:
            if words == clean:
                Klacht_status= False
                print(f'>>Klacht>>{words} is equal to {clean}')
    
    if Titel_status == False or Klacht_status == False:
        cursor.execute(f'''INSERT INTO klachten (titel,klacht,status) VALUES ('{Titel}','{Klacht}', 0);''')
        conn.commit()
    elif Titel_status != False and Klacht_status != False:
        cursor.execute(f'''INSERT INTO klachten (titel,klacht,status) VALUES ('{Titel}','{Klacht}', 1);''')
        conn.commit()
    else:
        print('error')

#moderator('vervelend kut ding','test ding')