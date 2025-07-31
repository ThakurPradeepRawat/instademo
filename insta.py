import psycopg2
DATABASE_URL = "postgresql://instadb_22cb_user:T2hXnPFMuju53ZrXTbMRZmEIDIl32RI5@dpg-d25kkfh5pdvs73dn0n2g-a.oregon-postgres.render.com/instadb_22cb"
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, name , passwor FROM users")
rows = cur.fetchall()
cur.close()
conn.close()
print("data")
print({
        'users': [{'id': row[0], 'name': row[1] , "password" : row[2]} for row in rows]
    })
print("close_connection")