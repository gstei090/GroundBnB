import psycopg2

#connect to the db 
con = psycopg2.connect(
            host = "web0.site.uottawa.ca",
            port = "15432",
            database="",
            user = "" ,
            password = "")

#cursor 
cur = con.cursor()

#execute query example
cur.execute("select aname, style from artist.styles")

rows = cur.fetchall()

for r in rows:
    print (f"aname {r[0]} style {r[1]}")

#close the cursor
cur.close()

#close the connection
con.close()