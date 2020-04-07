import psycopg2

#connect to the db 
def connect_to_database():

    connection = psycopg2.connect(
        host = "web0.site.uottawa.ca",
        port = "15432",
        database="",
        user = "" ,
        password = "",
        options= "-c search_path=groundbnb")
    return connection


def execute_query(query_string):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query_string)
    rows = None
    try:
        rows = cursor.fetchall()
    except:
        print('Nothing to fetch')
    connection.commit()
    cursor.close()
    connection.close()
    return rows
