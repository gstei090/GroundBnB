import psycopg2

#connect to the db 
def connect_to_database():

    connection = psycopg2.connect(
        host = "web0.site.uottawa.ca",
        port = "15432",
        database="",
        user = "" ,
        password = "")
    return connection


def execute_query(query_string):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query_string)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


# example
# con = connect_to_database()
# test_string = "SELECT * FROM laboratories.artist"
# res = execute_query(con, test_string)
# print(res)
# close_connection(con)